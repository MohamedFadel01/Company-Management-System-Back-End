from datetime import date

from companies.models import Company
from departments.models import Department
from django.test import TestCase
from employees.models import Employee


class EmployeeModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Test Company")
        self.department = Department.objects.create(
            company=self.company, name="Engineering"
        )

    def test_create_employee(self):
        employee = Employee.objects.create(
            company=self.company,
            department=self.department,
            name="John Doe",
            email="john@example.com",
            mobile_number="1234567890",
            address="123 Main St",
            designation="Software Engineer",
        )
        self.assertEqual(employee.name, "John Doe")
        self.assertEqual(employee.designation, "Software Engineer")
        self.assertEqual(employee.days_employed, 0)

    def test_days_employed_calculation(self):
        hired_on = date(2023, 1, 1)
        employee = Employee.objects.create(
            company=self.company,
            department=self.department,
            name="John Doe",
            email="john@example.com",
            mobile_number="1234567890",
            address="123 Main St",
            designation="Software Engineer",
            hired_on=hired_on,
        )
        self.assertGreater(employee.days_employed, 0)
