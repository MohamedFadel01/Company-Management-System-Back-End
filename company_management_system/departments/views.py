from departments.models import Department
from departments.serializers import DepartmentSerializer
from rest_framework import viewsets


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
