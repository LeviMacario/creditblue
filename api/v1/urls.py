from django.urls import path
from rest_framework.routers import DefaultRouter

from api.v1.user import views as user_views


router = DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    path('auth_login/', user_views.ObtainAuthToken.as_view()),
]