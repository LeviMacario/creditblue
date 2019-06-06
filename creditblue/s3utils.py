import os
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings 
from django.utils.functional import SimpleLazyObject

StaticRootS3Boto3Storage = lambda: S3Boto3Storage(location='static')
MediaRootS3Boto3Storage  = lambda: S3Boto3Storage(location='media')

ACCESS_KEY = getattr(settings, 'AWS_ACCESS_KEY_ID', None)
SECRET_KEY = getattr(settings, 'AWS_SECRET_ACCESS_KEY', None)


class MediaS3Boto3Storage(S3Boto3Storage):
    location = 'media'


class FixedS3Boto3Storage(S3Boto3Storage):
    def _get_access_keys(self):
        """
        Gets the access keys to use when accessing S3. If none
        are provided to the class in the constructor or in the
        settings then get them from the environment variables.
        """
        access_key = ACCESS_KEY
        secret_key = SECRET_KEY

        if not access_key or not secret_key:
            access_key = os.environ.get('AWS_ACCESS_KEY_ID')
            secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

        if access_key and secret_key:
            # Both were provided, so use them
            return access_key, secret_key

        return None, None