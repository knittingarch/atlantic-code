from rest_framework import serializers
from .models import Customer, Gift, Subscription


class GiftSerializer(serializers.ModelSerializer):
  class Meta:
    model = Gift
    fields = ['plan_name', 'price', 'recipient_email']

class SubscriptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subscription
    fields = ['plan_name', 'price']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
  gifts = GiftSerializer(many=True, read_only=True)
  subscriptions = SubscriptionSerializer(many=True, read_only=True)

  class Meta:
    model = Customer
    fields = ('id', 'first_name', 'last_name', 'address_1', 'address_2', 'city', 'state', 'postal_code', 'gifts', 'subscriptions')
