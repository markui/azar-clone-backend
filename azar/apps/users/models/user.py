import json

import six
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

__all__ = (
    'User',
    'FacebookUserProfile',
    'VipUser',
)

from django.contrib.auth.base_user import BaseUserManager


# Custom User Manager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, facebook_user_id, **extra_fields):
        """
        Creates and saves a User with the given "username" or "facebook_user_id"

        The User MUST HAVE either a "username" or "facebook_user_id"

        User.objects.create_user(username="markkim", password="12345678")
        User.objects.create_user(facebook_user_id="sadfa123afadf")
        """
        if username and facebook_user_id:
            raise ValueError('The username and facebook_user_id cannot be given at the same time when creating a user')
        if not username and not facebook_user_id:
            raise ValueError('Either the username or facebook_user_id is required')
        # Django 기본 유저(username) 생성
        if username:
            if password is None:
                raise ValueError("The 'password' field is required for users using django username")
            username = self.model.normalize_username(username)
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
        # Facebook 유저 생성
        elif facebook_user_id:
            # 1. User 생성
            user = self.model(is_facebook_user=True, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            # 2. 해당 User와 1대1 관계의 FacebookUserProfile 생성
            FacebookUserProfile.objects.create(user=user, facebook_user_id=facebook_user_id)
        return user

    def create_user(self, username=None, password=None, facebook_user_id=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, facebook_user_id, **extra_fields)

    def create_superuser(self, username, password, facebook_user_id=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, facebook_user_id, **extra_fields)


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    """
    Required Fields for creating a User by ".create_user" method:
    1. username OR facebook_user_id

    Required Fields (Form/Serializers)
    2. country
    3. time_zone
    4. language

    cf) birth_year, gender, 필수 수집 필드는 API 단에서 permissions로 처리하여
    Form Field가 있는 페이지로 유저를 Redirect 시켜서 처리한다
    """
    # Choices
    ## Gender Choices
    MALE = 'M'
    FEMALE = 'F'
    UNSPECIFIED = 'U'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNSPECIFIED, 'Unspecified')
    )
    ## Birth-Year Choices
    BIRTH_YEAR_CHOICES = [
        (year, year)
        for year
        in range(1900, timezone.localtime().year + 1)
    ]
    ## Country Choices (ISO 3166-1 alpha-2 format)
    iso_2_countries_mapping_data = json.loads(open(settings.ISO_2_COUNTRIES_MAPPING_FILE).read())
    COUNTRY_CHOICES = iso_2_countries_mapping_data.items()

    # Database Fields
    ## Database Fields - User Specific
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=20,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        blank=True,
        null=True
    )
    nickname = models.CharField(max_length=20, unique=True, blank=True, null=True,
                                help_text=_("Azar 내에서 다른 사용자들을 검색하는데 필요한 고유 Azar ID"))
    birth_year = models.PositiveSmallIntegerField(choices=BIRTH_YEAR_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    # location & time
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=100, blank=True)
    time_zone = models.CharField(max_length=50)
    language = models.CharField(max_length=10)

    # 후에, profile_image가 blank일 때 default로 AWS S3에서 정해진 프로필 이미지로 불러오도록 CustomImageField를 사용해야함
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    gem_total_count = models.IntegerField(default=0)
    ## Custom User Type
    is_facebook_user = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)

    ## Django User Type
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    ## Database Fields - User Relations

    # 현재 유저가 친구 신청을 보낸 유저 목록
    who_friend_request_to = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        # 현재 유저에게 친구 신청을 보낸 유저 목록
        related_name='who_friend_request_from',
        through='FriendInvitation',
        through_fields=('source', 'target')
    )
    # 현재 유저의 모든 친구 목록 (친구관계가 확정된 친구들)
    friends = models.ManyToManyField(
        'self',
        blank=True
    )

    # 현재 유저가 엄지척을 보낸 유저 목록
    who_thumbsup_to = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        # 현재 유저에게 엄지척을 보낸 유저 목록
        related_name='who_thumbsup_from',
        through='ThumbsUp',
        through_fields=('source', 'target')
    )
    # 현재 유저가 신고한 유저 목록
    who_report_to = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        # 현재 유저를 신고한 유저 목록
        related_name='who_report_from',
        through='Report',
        through_fields=('source', 'target')
    )

    # Custom User Manager
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        if self.username:
            if self.is_superuser:
                return f'type: superuser / username: {self.username}'
            return f'type: django / username: {self.username}'
        else:
            return f'type: facebook / facebook_user_id: {self.facebook_user_profile.facebook_user_id}'

    # save method override

    # get_absolute_url

    # Custom Methods
    def get_short_name(self):
        """
        기본 admin 페이지에서 "Welcome, [get_short_name()]" 부분에서 호출되는 함수
        :return:
        """
        "Returns the short name for the user."
        return self.username

    def filled_required_fields(self):
        """
        birth_year, gender,
        2개의 필수적으로 수집해야 하는 user info를
        가지고 있는지를 판단해주는 custom method
        :return: Boolean
        """
        pass


class FacebookUserProfile(models.Model):
    """
    OneToOneRelation With Facebook Users with "is_facebook_user=True"

    Stores Facebook-Specific Info fetched from the "Facebook Graph API"
    """
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name='facebook_user_profile')
    facebook_user_id = models.CharField(max_length=128)
    email = models.EmailField(unique=True, blank=True, null=True)
    # friends


class VipUser(User):
    """
    Proxy Model of User
    """
    pass
