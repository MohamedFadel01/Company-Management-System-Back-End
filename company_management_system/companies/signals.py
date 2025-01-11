from companies.models import Company
from departments.models import Department
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from employees.models import Employee
from projects.models import Project


@receiver(post_save, sender=Department)
@receiver(post_delete, sender=Department)
def update_company_department_count(sender, instance, **kwargs):
    company = instance.company
    company.update_counts()


@receiver(post_save, sender=Employee)
@receiver(post_delete, sender=Employee)
def update_company_employee_count(sender, instance, **kwargs):
    company = instance.company
    company.update_counts()


@receiver(post_save, sender=Project)
@receiver(post_delete, sender=Project)
def update_company_project_count(sender, instance, **kwargs):
    company = instance.company
    company.update_counts()
