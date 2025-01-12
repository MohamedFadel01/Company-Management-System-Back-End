from accounts.models import User
from companies.models import Company
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CompanyAPITest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin", password="adminpass", role="ADMIN"
        )
        self.client.force_authenticate(user=self.admin_user)
        self.company = Company.objects.create(name="Test Company")

    def test_list_companies(self):
        response = self.client.get(reverse("company-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_company(self):
        data = {
            "name": "New Company",
            "number_of_departments": 0,
            "number_of_employees": 0,
            "number_of_projects": 0,
        }
        response = self.client.post(reverse("company-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 2)
