from accounts.models import User
from accounts.permissions import IsAdmin, IsEmployee, IsManager
from django.test import RequestFactory, TestCase


class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="testuser", password="testpass", role="EMPLOYEE"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.role, "EMPLOYEE")
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username="admin", password="adminpass", role="ADMIN"
        )
        self.assertEqual(admin_user.role, "ADMIN")
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class PermissionsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.admin_user = User.objects.create_user(
            username="admin", password="adminpass", role="ADMIN"
        )
        self.manager_user = User.objects.create_user(
            username="manager", password="managerpass", role="MANAGER"
        )
        self.employee_user = User.objects.create_user(
            username="employee", password="employeepass", role="EMPLOYEE"
        )

    def test_is_admin_permission(self):
        request = self.factory.get("/")
        request.user = self.admin_user
        permission = IsAdmin()
        self.assertTrue(permission.has_permission(request, None))

        request.user = self.manager_user
        self.assertFalse(permission.has_permission(request, None))

        request.user = self.employee_user
        self.assertFalse(permission.has_permission(request, None))

    def test_is_manager_permission(self):
        request = self.factory.get("/")
        request.user = self.admin_user
        permission = IsManager()
        self.assertFalse(permission.has_permission(request, None))

        request.user = self.manager_user
        self.assertTrue(permission.has_permission(request, None))

        request.user = self.employee_user
        self.assertFalse(permission.has_permission(request, None))

    def test_is_employee_permission(self):
        request = self.factory.get("/")
        request.user = self.admin_user
        permission = IsEmployee()
        self.assertFalse(permission.has_permission(request, None))

        request.user = self.manager_user
        self.assertFalse(permission.has_permission(request, None))

        request.user = self.employee_user
        self.assertTrue(permission.has_permission(request, None))
