from companies.models import Company
from django.db import models


class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number_of_employees = models.IntegerField(default=0)
    number_of_projects = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def update_counts(self):
        self.number_of_employees = self.employee_set.count()
        self.number_of_projects = self.project_set.count()
        self.save()
