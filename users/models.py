from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
from core.models import TimeStampedModel

TZ = timezone.get_current_timezone()


def content_file_name(instance, filename):
    return '/'.join(['uploads/users/avatars',
                    slugify(instance.pk),
                    "{0}".format(filename)])


class User(AbstractUser, TimeStampedModel):
    avatar = models.ImageField(
        'Foto do perfil',
        upload_to=content_file_name,
        null=True,
        blank=True
    )
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    def __str__(self):
        return '{0}'.format(self.email)

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)