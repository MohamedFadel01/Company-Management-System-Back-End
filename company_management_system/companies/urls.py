from companies.views import CompanyViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", CompanyViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
