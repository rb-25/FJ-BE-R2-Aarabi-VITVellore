from django.conf import settings
from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from fj_finance_tracker.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    re_path("users/", include("fj_finance_tracker.users.api.urls")),
    #re_path("core/", include("fj_finance_tracker.core.api.urls")),
]

app_name = "api"
urlpatterns += router.urls

