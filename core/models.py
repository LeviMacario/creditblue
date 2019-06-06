from datetime import datetime
from django.db import models
from django.conf import settings
from .managers import DeleteManager
from django.utils import timezone


TZ = timezone.get_current_timezone()


class DeleteModel(models.Model):
    deleted_at = models.DateTimeField(
        'Excluído em',
        default=None,
        null=True,
        blank=True
    )

    objects = DeleteManager()

    class Meta:
        abstract = True


class TimeStampedModel(DeleteModel):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Updates timestamps on save"""
        if not self.id:
            self.created_at = datetime.now(tz=TZ)
        self.updated_at = datetime.now(tz=TZ)
        return super(TimeStampedModel, self).save(*args, **kwargs)


class StatusDate(TimeStampedModel):
    status = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True