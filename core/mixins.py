from django.utils import timezone
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.exceptions import ImproperlyConfigured
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import View
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


TZ = timezone.get_current_timezone()


class CSRFExemptMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return csrf_exempt(view)


class SoftDeletionMixin(SingleObjectMixin, View):
    """
    A mixin providing the ability to soft delete objects
    """
    success_url = None

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.deleted_at = datetime.now(tz=TZ)
        self.object.save(update_fields=['deleted_at'])
        messages.add_message(
            request, messages.SUCCESS,
            '{0} excluído com sucesso!'.format(self.object)
        )
        return HttpResponseRedirect(success_url)

    # Add support for browsers which only accept GET and POST for now.
    def post(self, request, *args, **kwargs):
        if request.user == self.get_object():
            messages.add_message(
                request, messages.ERROR,
                'Operação não permitida!'
            )
            return HttpResponseRedirect(self.success_url)
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        if self.success_url:
            return self.success_url.format(**self.object.__dict__)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url."
            )