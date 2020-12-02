from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Customer
    fields = ('first_name', 'last_name', 'address_1', 'address_2', 'city', 'state', 'postal_code')
