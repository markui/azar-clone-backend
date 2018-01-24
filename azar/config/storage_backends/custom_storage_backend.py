import os

from django.core.files.storage import FileSystemStorage

django_settings = os.environ['DJANGO_SETTINGS_MODULE']


# S3 Private Mediafiles
def PrivateMediaStorage():
    """
    local, production 환경에 따라
    서로 다른 PrivateMediaStorage를 사용하기 위한 함수

    :return: Storage Class for Media Files
    """
    # local - django 기본 Media Storage / MEDIA_ROOT
    if django_settings == 'config.settings.local':
        return FileSystemStorage()
    # production - S3 PrivateMediaStorage
    elif django_settings == 'config.settings.production':
        from .dj_storage_backend import S3PrivateMediaStorage
        return S3PrivateMediaStorage()
