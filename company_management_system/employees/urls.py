from django.urls import include, path
from employees.views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", EmployeeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
