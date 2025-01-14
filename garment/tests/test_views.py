from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

from accounts.factories import PublisherFactory
from garment.factories import GarmentFactory
from django.urls import reverse
from faker import Faker

class GarmentViewTests(APITestCase):
    @classmethod
    def setUp(self):
        """
        Set up the test by creating a user, defining URLs, creating a Faker instance, and creating an APIClient instance.
        """
        # Create a user
        self.user = PublisherFactory.create()

        # Create garments using the GarmentFactory
        self.garment1 = GarmentFactory.create(size=1, type=2, price=100)
        self.garment2 = GarmentFactory.create(size=2, type=1, price=150)
        self.garment3 = GarmentFactory.create(size=2, type=1, price=200)

        # Define Faker instance
        self.faker = Faker()

        # Define the APIClient
        self.client = APIClient()

        # Define the URL
        self.create_url = reverse('create_garment')
        self.list_url = reverse('get_paginated_garment')
        self.detail_url = reverse('get_garment_detail', kwargs={'id': self.garment1.id})
        self.delete_url = reverse('delete_garment', kwargs={'id': self.garment1.id})
        self.update_url = reverse('update_garment', kwargs={'id': self.garment1.id})

    def authenticate_user(self):
        """
        Authenticate the user by generating an access token and setting it in the request header.
        """
        # Generate an access token for the user
        token = AccessToken.for_user(self.user)

        # Set the token in the request header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_get_all_garments_authenticated(self):
        """Test retrieving all garments as an authenticated user."""
        self.authenticate_user()

        response = self.client.get(self.list_url)

        # Assert response status and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)  # Pagination results key
        self.assertEqual(len(response.data['results']), 3)  # All garments returned

    def test_filter_garments_by_size(self):
        """Test filtering garments by size."""
        self.authenticate_user()

        response = self.client.get(self.list_url, {'size': 2})

        # Assert response status and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Only garments of size 2

    def test_filter_garments_by_type(self):
        """Test filtering garments by size."""
        self.authenticate_user()

        response = self.client.get(self.list_url, {'type': 1})

        # Assert response status and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Only garments of size M

    def test_filter_garments_by_price_range(self):
        """Test filtering garments by price range."""
        self.authenticate_user()

        response = self.client.get(self.list_url, {'price_min': 100, 'price_max': 150})

        # Assert response status and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Only garments within price range

    def test_pagination(self):
        """Test pagination for garments."""
        self.authenticate_user()

        response = self.client.get(self.list_url, {'page': 1})

        # Assert response status and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertTrue(len(response.data['results']) <= 10)  # Pagination size
