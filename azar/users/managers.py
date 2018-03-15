from django.contrib.auth.base_user import BaseUserManager

# Custom User Manager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, facebook_user_id, **extra_fields):
        """
        Creates and saves a User with the given "username" or "facebook_user_id"

        The User MUST HAVE either a "username" or "facebook_user_id"

        User.objects.create_user(username="azar_lover", password="sg5909sg")
        User.objects.create_user(facebook_user_id="sadfa")
        """
        if not username and not facebook_user_id:
            raise ValueError('Either the username or facebook_user_id is required')
        if username:
            username = self.model.normalize_username(username)
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
        elif facebook_user_id:
            pass

        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, facebook_user_id=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, facebook_user_id, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)
