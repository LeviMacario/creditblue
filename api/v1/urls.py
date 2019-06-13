from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.user import views as user_views
from api.v1.contract import views as contract_views


router = DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    path('auth_login/', user_views.ObtainAuthToken.as_view()),
    path('loan_contracts/', contract_views.LoanContractListCreate.as_view()),
    path(
        'loan_contracts/<int:pk>/',
        contract_views.LoanContractDetail.as_view()
    ),
    path('payments/', contract_views.LoanContractPaymentListCreate.as_view()),
    # path('payments/<int:pk>/', contract_views.LoanContractPaymentDetail.as_view()),
]
