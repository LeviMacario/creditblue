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