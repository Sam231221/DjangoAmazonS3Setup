from storages.backends.s3boto3 import S3Boto3Storage



class StaticStorage(S3Boto3Storage):
    #aws location of where staticfiles are?
    location = 'staticfiles'
    default_acl = None


class PublicMediaStorage(S3Boto3Storage):
    #aws location of where mediafiles should be stored?
    location = 'mediafiles'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    #aws location of where mediafiles should be stored?
    location = 'privatefiles'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False