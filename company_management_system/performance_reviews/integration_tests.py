from accounts.models import User
from companies.models import Company
from departments.models import Department
from django.urls import reverse
from employees.models import Employee
from performance_reviews.models import PerformanceReview
from rest_framework import status
from rest_framework.test import APITestCase


class PerformanceReviewAPITest(APITestCase):
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
        self.review = PerformanceReview.objects.create(
            employee=self.employee, stage="PENDING"
        )

    def test_transition_to_scheduled_as_manager(self):
        self.client.force_authenticate(user=self.manager)
        data = {"stage": "SCHEDULED"}
        response = self.client.post(
            reverse("review-transition", args=[self.review.id]), data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.review.refresh_from_db()
        self.assertEqual(self.review.stage, "SCHEDULED")

    def test_transition_to_approved_as_manager(self):
        self.client.force_authenticate(user=self.manager)
        data = {"stage": "APPROVED"}
        response = self.client.post(
            reverse("review-transition", args=[self.review.id]), data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.review.refresh_from_db()
        self.assertEqual(self.review.stage, "PENDING")
