from accounts.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserAPITest(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin", password="adminpass", role="ADMIN"
        )
        self.manager_user = User.objects.create_user(
            username="manager", password="managerpass", role="MANAGER"
        )
        self.employee_user = User.objects.create_user(
            username="employee", password="employeepass", role="EMPLOYEE"
        )

    def test_list_users_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_user_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        data = {"username": "newuser", "password": "newpass", "role": "EMPLOYEE"}
        response = self.client.post(reverse("user-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 4)
