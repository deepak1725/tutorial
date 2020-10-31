import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import RequestsClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase


class TestAPI(APITestCase):

    def test_get_users(self):
        """Test Get Users"""
        url = '/api/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_users(self):
        """Test Create Users"""
        url = '/api/users/'
        response = self.client.post(url, {'username': 'test'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

