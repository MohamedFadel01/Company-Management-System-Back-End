from companies.models import Company
from departments.models import Department
from django.test import TestCase
from employees.models import Employee
from projects.models import Project


class DepartmentModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")

    def test_create_department(self):
        department = Department.objects.create(company=self.company, name="Engineering")
        self.assertEqual(department.name, "Engineering")
        self.assertEqual(department.number_of_employees, 0)
        self.assertEqual(department.number_of_projects, 0)

    def test_update_counts(self):
        department = Department.objects.create(company=self.company, name="Engineering")
        employee = Employee.objects.create(
            company=self.company,
            department=department,
            name="John Doe",
            email="john@example.com",
            mobile_number="1234567890",
            address="123 Main St",
            designation="Software Engineer",
        )
        project = Project.objects.create(
            company=self.company,
            department=department,
            name="Project X",
            description="A new project",
            start_date="2023-01-01",
            end_date="2023-12-31",
        )
        project.assigned_employees.add(employee)

        department.update_counts()
        self.assertEqual(department.number_of_employees, 1)
        self.assertEqual(department.number_of_projects, 1)
