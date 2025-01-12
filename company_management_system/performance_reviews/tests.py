from accounts.models import User
from companies.models import Company
from departments.models import Department
from django.test import TestCase
from employees.models import Employee
from performance_reviews.models import PerformanceReview


class PerformanceReviewModelTest(TestCase):
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
        self.manager = User.objects.create_user(
            username="manager", password="managerpass", role="MANAGER"
        )

    def test_create_performance_review(self):
        review = PerformanceReview.objects.create(
            employee=self.employee, stage="PENDING"
        )
        self.assertEqual(review.stage, "PENDING")
        self.assertEqual(review.employee.name, "John Doe")

    def test_transition_to_valid_stage(self):
        review = PerformanceReview.objects.create(
            employee=self.employee, stage="PENDING"
        )
        self.assertTrue(review.transition_to("SCHEDULED", self.manager))
        self.assertEqual(review.stage, "SCHEDULED")

    def test_transition_to_invalid_stage(self):
        review = PerformanceReview.objects.create(
            employee=self.employee, stage="PENDING"
        )
        self.assertFalse(review.transition_to("APPROVED", self.manager))
        self.assertEqual(review.stage, "PENDING")
