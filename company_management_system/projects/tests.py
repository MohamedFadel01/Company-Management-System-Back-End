from companies.models import Company
from departments.models import Department
from django.test import TestCase
from employees.models import Employee
from projects.models import Project


class ProjectModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.department = Department.objects.create(
            company=self.company, name="Engineering"
        )
        self.employee = Employee.objects.create(
            company=self.company,
            department=self.department,
            name="John Doe",
            email="john@example.com",
            mobile_number="1234567890",
            address="123 Main St",
            designation="Software Engineer",
        )

    def test_create_project(self):
        project = Project.objects.create(
            company=self.company,
            department=self.department,
            name="Project X",
            description="A new project",
            start_date="2023-01-01",
            end_date="2023-12-31",
        )
        project.assigned_employees.add(self.employee)
        self.assertEqual(project.name, "Project X")
        self.assertEqual(project.assigned_employees.count(), 1)
