import json

import six
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    """
    Required Fields for creating a User by ".create_user" method
    - username OR facebook_user_id
    - birth_year
    - gender
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
    ## User Specific
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()

    # Azar 내에서 다른 사용자들을 검색하는데 필요한 고유 "Azar ID" 뜻함
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
    nickname = models.CharField(max_length=20, unique=True, blank=True, null=True)
    birth_year = models.PositiveSmallIntegerField(choices=BIRTH_YEAR_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=UNSPECIFIED)
    # location & time
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=100, blank=True)
    time_zone = models.CharField(max_length=50)
    language = models.CharField(max_length=10)

    # 후에, profile_image가 blank일 때 default로 AWS S3에서 정해진 이미지를 불러오도록 CustomImageField로 수정해야함
    profile_image = models.ImageField(upload_to=f'profile/', blank=True)
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

    # Database Fields - Relations

    # Custom User Manager
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username or self.facebookuserprofile.facebook_user_id
        # save
        # get_absolute_url
        # custom methods


class FacebookUserProfile(models.Model):
    """
    OneToOneRelation With Facebook Users with "is_facebook_user=True"

    Stores Facebook-Specific Info fetched from the "Facebook Graph API"
    """
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    facebook_user_id = models.CharField(max_length=128)
    email = models.EmailField(unique=True, blank=True, null=True)
    # friends


class VipUser(User):
    """
    Proxy Model of User
    """
    pass
