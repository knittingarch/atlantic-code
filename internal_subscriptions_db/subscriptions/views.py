# from django.shortcuts import render

from rest_framework import viewsets

from .serializers import (
  CustomerSerializer,
  GiftSerializer,
  SubscriptionSerializer
)

from .models import Customer, Gift, Subscription

class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class GiftViewSet(viewsets.ModelViewSet):
  queryset = Gift.objects.all()
  serializer_class = GiftSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
  queryset = Subscription.objects.all()
  serializer_class = SubscriptionSerializer
