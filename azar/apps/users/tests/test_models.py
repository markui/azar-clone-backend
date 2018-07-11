from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import User, FacebookUserProfile

__all__ = (
    'UserModelTest',
)


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods
        :return:
        """
        User.objects.create_user(
            username="john",
            password="12345678"
        )
        User.objects.create_user(
            facebook_user_id="asd123"
        )
        User.objects.create_superuser(
            username="markkim",
            password="12345678"
        )

    def test_user_is_auth_user_model(self):
        """
        settings.AUTH_USER_MODEL이 Custom User와 일치하는지 확인
        :return:
        """
        self.assertEqual(get_user_model(), User)

    def test_create_django_user(self):
        """
        Django 기본 username 사용하는 유저 생성 테스트
        :return:
        """
        django_user = User.objects.create_user(
            username="david",
            password="12345678"
        )
        self.assertIsInstance(django_user, User)
        self.assertEqual(django_user.is_facebook_user, False)

    def test_create_facebook_user(self):
        """
        Facebook 유저 생성 테스트
        :return:
        """
        facebook_user = User.objects.create_user(
            facebook_user_id="asdf1234"
        )
        self.assertIsInstance(facebook_user, User)
        self.assertEqual(facebook_user.is_facebook_user, True)

    def test_create_superuser(self):
        """
        Superuser 생성 테스트
        :return:
        """
        superuser = User.objects.create_superuser(
            username="danielkim",
            password="12345678"
        )
        self.assertIsInstance(superuser, User)
        self.assertEqual(superuser.is_staff, True)
        self.assertEqual(superuser.is_superuser, True)

    def test_create_both_django_and_facebook_type_user(self):
        """
        Django username을 사용하면서, facebook_user_id 또한 인자로 줘,
        상호배제 관계에 있는 두개의 user type을 모두 만족하는 User를 생성하려는 경우
        오류 발생 테스트
        :return:
        """
        try:
            User.objects.create_user(username="2typeuser", password="1234", facebook_user_id="as1234")
        except Exception as e:
            self.assertIsInstance(e, ValueError)
            self.assertEqual(str(e),
                             'The username and facebook_user_id cannot be given at the same time when creating a user')

    def test_create_user_with_no_username_and_no_facbook_user_id(self):
        """
        Django username 기본 타입 유저, Facebook User 생성에 필요한 인자를
        하나도 주지 않고 User를 생성하려는 경우
        오류 발생 테스트
        :return:
        """
        pass

    def test_create_django_user_with_username_and_no_password(self):
        """
        Django username 기본 타입 유저를 생성하는 데, username은 입력했으나 password는
        입력하지 않은 경우
        오류 발생 테스트
        :return:
        """
        pass

    def test_create_facebook_user_auto_creates_facebook_user_profile(self):
        """
        Facebook 유저를 생성하면, 1대1 관계로 연결된 FacebookUserProfile를 자동으로 생성하는지 여부 테스트
        :return:
        """
        # facebook_user = User.objects.create_user(facebook_user_id="asdfg12345")
        facebook_user = User.objects.create_user(facebook_user_id="asdfg12345")
        facebook_user_profile = facebook_user.facebook_user_profile
        self.assertIsInstance(facebook_user_profile, FacebookUserProfile)
        self.assertEqual(facebook_user_profile.facebook_user_id, "asdfg12345")

    def test_user_verbose_name_singular(self):
        """
        User Meta verbose_name 테스트
        :return:
        """
        superuser = User.objects.get(username="markkim")
        field_label = superuser._meta.verbose_name
        self.assertEquals(field_label, 'user')

    def test_user_verbose_name_plural(self):
        """
        User Meta verbose_name_plural 테스트
        :return:
        """
        superuser = User.objects.get(username="markkim")
        field_label = superuser._meta.verbose_name_plural
        self.assertEquals(field_label, 'users')

    def test_string_representation_for_django_user(self):
        pass

    def test_string_representation_for_facebook_user(self):
        pass

    def test_string_representation_for_superuser(self):
        pass
