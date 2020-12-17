from rest_framework import serializers
from .models import Customer, Gift, Subscription


class GiftSerializer(serializers.ModelSerializer):
  class Meta:
    model = Gift
    fields = '__all__'

  def create(self, validated_data):
    gift = Gift.objects.create(**validated_data)
    return gift

class SubscriptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subscription
    fields = '__all__'

  def create(self, validated_data):
    subscription = Subscription.objects.create(**validated_data)
    return subscription

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
  gifts = GiftSerializer(many=True, required=False)
  subscriptions = SubscriptionSerializer(many=True, required=False)

  class Meta:
    model = Customer
    fields = '__all__'

  def create(self, validated_data):
    gift_data = validated_data.pop('gifts')
    subscription_data = validated_data.pop('subscriptions')
    customer = Customer.objects.create(**validated_data)
    customer.gifts.set(gift_data)
    customer.subscriptions.set(subscription_data)
    return customer
