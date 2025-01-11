from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    number_of_departments = models.IntegerField(default=0)
    number_of_employees = models.IntegerField(default=0)
    number_of_projects = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def update_counts(self):
        self.number_of_departments = self.department_set.count()
        self.number_of_employees = self.employee_set.count()
        self.number_of_projects = self.project_set.count()
        self.save()
