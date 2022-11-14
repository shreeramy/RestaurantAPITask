from http.cookies import SimpleCookie
from users.tests.factories import UserFactory
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class UserAuthTest(TestCase):
    def setUp(self):
        self.url = "account/api/"
        self.client = APIClient()
        self.user = UserFactory.create(email="testuser@testuser.com")

        self.admin_user = UserFactory.create(email="testadminuser@testuser.com")
        self.admin_user.is_staff = True
        self.admin_user.is_superuser = True
        self.admin_user.save()

    def test_unauthenticated_auth_info_post(self):
        """
        unauthenticated user should receive a 401 response when
        visiting pages that require login
        """

        response = self.client.post(reverse("employee_create"))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_auth_info_get(self):
        """
        authenticated user should receive a 200 response when
        visiting a page that requires authentication
        """
        token = RefreshToken.for_user(self.user)
        self.client.cookies = SimpleCookie({"authCookie": 
            str(token.access_token), "refreshCookie": str(token)})

        response = self.client.get(reverse("employee_create"))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_login(self):
        """
        login with invalid credentials should not be successful
        """

        account = {"email": "someemail@test.com", "password": "somepass"}

        response = self.client.post(reverse("access_token"), account)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_registration_and_confirmation_invalid_data(self):
        """
        Post Incvalid Data 
        """
        doula = {
            "email": "testuser1@registration.com",
            "first_name": "John",
            "last_name": "Doe",
            "phone_no": "+12345",
            "password1": "testpassword.1",
            "password2": "testpassword.1",
        }

        response = self.client.post(reverse("account_register"), 
                                             doula, format="json")
        self.assertEqual(response.status_code, 
            status.HTTP_400_BAD_REQUEST)


    def test_get_token_with_invalid_user_token(self):
        """
        get token of another user only by user who has permission to get token
        """

        data = {
            "email": self.user.email
        }
        res = self.client.post("access_token", data)
        self.assertEqual(res.status_code, 404)
