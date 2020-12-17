from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import CustomerFactory, GiftFactory, SubscriptionFactory
from .models import Customer, Gift, Subscription

class GiftTestCases(APITestCase):
    def setUp(self):
        self.gift = GiftFactory()

    def tearDown(self):
        self.gift.delete()

    def test_gift_GET_request(self):
        """
        Ensure we can retrieve a Gift object.
        """

        url = reverse('gift-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Gift.objects.get().plan_name, self.gift.plan_name)

    def test_gift_POST_request(self):
        """
        Ensure we can create a new Gift object.
        """

        url = reverse('gift-list')
        data = {
            'plan_name': 'Test Gift',
            'price': '9999',
            'recipient_email': 'test@test.com',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Gift.objects.count(), 2)
        self.assertEqual(
            Gift.objects.filter(plan_name='Test Gift').first().plan_name,
            'Test Gift'
        )

class SubscriptionTestCases(APITestCase):
    def setUp(self):
        self.subscription = SubscriptionFactory()

    def tearDown(self):
        self.subscription.delete()

    def test_subscription_GET_request(self):
        """
        Ensure we can retrieve a Subscription object.
        """

        url = reverse('subscription-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.get().plan_name, self.subscription.plan_name)

    def test_subscription_POST_request(self):
        """
        Ensure we can create a new Subscription object.
        """

        url = reverse('subscription-list')
        data = {
            'plan_name': 'Test Subscription',
            'price': '9999',
            'recipient_email': 'test@test.com',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 2)
        self.assertEqual(
            Subscription.objects.filter(plan_name='Test Subscription').first().plan_name,
            'Test Subscription'
        )

class CustomerTestCases(APITestCase):
    def test_get_customer(self):
        """
        Ensure we can retrieve an existing Customer object.
        """
        CustomerFactory()

        url = reverse('customer-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get().first_name, 'Betty')
        self.assertEqual(Customer.objects.get().last_name, 'Boop')

    def test_create_customer(self):
        """
        Ensure we can create a Customer object.
        """

        data = {
            'first_name': 'Beatrice',
            'last_name': 'Potter',
            'address_1': '123 Washington Street',
            'city': 'Milwaukee',
            'state': 'WI',
            'postal_code': '53212',
            'gifts': [],
            'subscriptions': [],
        }

        url = reverse('customer-list')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, 'Beatrice')
        self.assertEqual(Customer.objects.get().last_name, 'Potter')


    def test_create_customer_with_gift(self):
        """
        Ensure we can create a Customer object with a gift.
        """

        gift = GiftFactory()

        data = {
            'first_name': 'Beatrice',
            'last_name': 'Potter',
            'address_1': '123 Washington Street',
            'city': 'Milwaukee',
            'state': 'WI',
            'postal_code': '53212',
            'gifts': [gift],
            'subscriptions': [],
        }

        url = reverse('customer-list')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, 'Beatrice')
        self.assertEqual(Customer.objects.get().last_name, 'Potter')
