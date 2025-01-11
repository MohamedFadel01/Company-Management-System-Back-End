from departments.models import Department
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from employees.models import Employee
from projects.models import Project


@receiver(post_save, sender=Employee)
@receiver(post_delete, sender=Employee)
def update_department_employee_count(sender, instance, **kwargs):
    department = instance.department
    department.update_counts()


@receiver(post_save, sender=Project)
@receiver(post_delete, sender=Project)
def update_department_project_count(sender, instance, **kwargs):
    department = instance.department
    department.update_counts()
