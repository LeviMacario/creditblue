from django.db import models


class DeleteManager(models.Manager):
    def _apply_default(self, qs, deleted=True):
        '''Enable Inheritance of the Manager by modifying QuerySet'''
        return qs.filter(deleted_at__isnull=deleted)

    def get_queryset(self):
        qs = self._apply_default(super().get_queryset())
        return qs.order_by('-created_at')

    def excluded(self):
        qs = self._apply_default(super().get_queryset(), False)
        return qs.order_by('-created_at')

    def active(self):
        qs = self.get_queryset()
        return qs.filter(status=True)

    def inactive(self):
        qs = self.get_queryset()
        return qs.filter(status=False)


class InRangeMixin(DeleteManager):
    def in_range(self, field, from_date, to_date):
        queryset = self.get_queryset()
        query_filter = {
            '%s__gte' % field: from_date,
            '%s__lte' % field: to_date,
        }
        return queryset.filter(**query_filter)
