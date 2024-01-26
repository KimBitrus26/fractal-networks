from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.storage import get_storage_class


class StaticStorage(S3Boto3Storage):
    location = 'home/evaluation_test/static'
    default_acl = 'public-read'

    def __init__(self, *args, **kwargs):
        super(StaticStorage, self).__init__(*args, **kwargs)
        self.local_storage = get_storage_class("compressor.storage.CompressorFileStorage")()

    def save(self, name, content, max_length=None):
        self.local_storage._save(name, content)
        super(StaticStorage, self).save(name, self.local_storage._open(name))
        return name


class PublicMediaStorage(S3Boto3Storage):
    location = 'home/evaluation_test/media'
    default_acl = 'public-read'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    location = 'home/evaluation_test/private'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False
