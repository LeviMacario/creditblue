from rest_framework import generics, authentication, permissions
from api.v1.contract import serializers

from contracts.models import LoanContract, LoanContractPayment


class LoanContractListCreate(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.LoanContractSerializer

    def get_queryset(self):
        """
        This view should return a list of all the loan contracts for
        the user as determined by the token portion of the URL.
        """
        qs = LoanContract.objects.filter(responsible=self.request.user)
        return qs


class LoanContractPaymentListCreate(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.LoanContractPaymentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the payment loan contracts for
        the user as determined by the token portion of the URL.
        """
        qs = LoanContractPayment.objects.filter(
            loan_contract__responsible=self.request.user
        )
        return qs


class LoanContractDetail(generics.RetrieveAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.LoanContractSerializer
    model = LoanContract

    def get_queryset(self):
        """
        Return the `QuerySet` that will be used to look up the object.

        Note that this method is called by the default implementation of
        `get_object` and may not be called if `get_object` is overridden.
        """
        if self.queryset is None:
            if self.model:
                return self.model._default_manager.filter(
                    responsible=self.request.user
                )
            else:
                raise ImproperlyConfigured(
                    "%(cls)s is missing a QuerySet. Define "
                    "%(cls)s.model, %(cls)s.queryset, or override "
                    "%(cls)s.get_queryset()." % {
                        'cls': self.__class__.__name__
                    }
                )
        return self.queryset.filter(responsible=self.request.user)