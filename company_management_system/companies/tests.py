from companies.models import Company
from departments.models import Department
from django.test import TestCase
from employees.models import Employee
from projects.models import Project


class CompanyModelTest(TestCase):
    def test_create_company(self):
        company = Company.objects.create(name="Test Company")
        self.assertEqual(company.name, "Test Company")
        self.assertEqual(company.number_of_departments, 0)
        self.assertEqual(company.number_of_employees, 0)
        self.assertEqual(company.number_of_projects, 0)

    def test_update_counts(self):
        company = Company.objects.create(name="Test Company")
        department = Department.objects.create(company=company, name="Engineering")
        employee = Employee.objects.create(
            company=company,
            department=department,
            name="John Doe",
            email="john@example.com",
            mobile_number="1234567890",
            address="123 Main St",
            designation="Software Engineer",
        )
        project = Project.objects.create(
            company=company,
            department=department,
            name="Project X",
            description="A new project",
            start_date="2023-01-01",
            end_date="2023-12-31",
        )
        project.assigned_employees.add(employee)

        company.update_counts()
        self.assertEqual(company.number_of_departments, 1)
        self.assertEqual(company.number_of_employees, 1)
        self.assertEqual(company.number_of_projects, 1)
