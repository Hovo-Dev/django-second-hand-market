from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from accounts.models import Publisher

from django.urls import reverse
from accounts.factories import PublisherFactory
from faker import Faker

class AccountViewTests(APITestCase):
    @classmethod
    def setUp(self):
        """
        Set up the test by creating a user, defining URLs, creating a Faker instance, and creating an APIClient instance.
        """
        # Create a user using the PublisherFactory
        self.user = PublisherFactory.create()

        # Define URLs
        self.register_url = reverse('register')  # Adjust with the actual URL name
        self.login_url = reverse('login')  # Adjust with the actual URL name
        self.profile_url = reverse('profile')  # Adjust with the actual URL name
        self.logout_url = reverse('logout')  # Adjust with the actual URL name

        # Define Faker instance
        self.faker = Faker()

        # Create an APIClient instance
        self.client = APIClient()

    def authenticate_user(self):
        """
        Authenticate the user by generating an access token and setting it in the request header.
        """

        # Generate an access token for the user
        token = AccessToken.for_user(self.user)

        # Set the token in the request header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_register_view(self):
        """
        Test the register view by generating random data, making a POST request to the register view, and checking the response.
        """

        # Generate random data using Faker
        username = self.faker.user_name()
        full_name = self.faker.name()
        address = self.faker.address()
        password = self.faker.password(length=12, special_chars=True, digits=True, upper_case=True)

        # Prepare the data for the API request
        data = {
            'username': username,
            'full_name': full_name,
            'password': password,
            'address': address
        }

        # Make a POST request to the register view
        response = self.client.post(self.register_url, data, format='json')

        # Assert the response status and check returned data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user']['username'], username)
        self.assertEqual(response.data['user']['address'], address)
        self.assertEqual(response.data['user']['full_name'], full_name)

        # Check if the user is created in the database
        publisher = Publisher.objects.get(username=username)
        self.assertIsNotNone(publisher)

        # Optionally, check if the response includes the token
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_profile_view(self):
        """
        Test the profile view by authenticating the user and making a GET request to the profile view.
        """
        # Authenticate the user
        self.authenticate_user()

        # Call the profile view
        response = self.client.get(self.profile_url)

        # Check the response status and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('username', response.data)
        self.assertIn('full_name', response.data)
        self.assertIn('address', response.data)

        # Check if the user data is correct
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['full_name'], self.user.full_name)
        self.assertEqual(response.data['address'], self.user.address)
