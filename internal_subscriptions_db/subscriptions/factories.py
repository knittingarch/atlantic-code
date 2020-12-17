import factory
from factory.django import DjangoModelFactory
from .models import Customer, Gift, Subscription

class GiftFactory(DjangoModelFactory):
  class Meta:
    model = Gift

  plan_name = factory.Sequence(lambda n: 'gift%d' % n)
  price = "7999"
  recipient_email = factory.Sequence(lambda n: 'user%d@test.com' % n)

class SubscriptionFactory(DjangoModelFactory):
  class Meta:
    model = Subscription

  plan_name = factory.Sequence(lambda n: 'subscription%d' % n)
  price = "2999"

class CustomerFactory(DjangoModelFactory):
  class Meta:
    model = Customer

  first_name = 'Betty'
  last_name = 'Boop'
  address_1 = '123 Washington Street'
  address_2 = ''
  city = 'Milwaukee'
  state = 'WI'
  postal_code = '53212'

  gifts = factory.RelatedFactory(
    GiftFactory,
    factory_related_name='customer',
  )

  subscriptions = factory.RelatedFactory(
    SubscriptionFactory,
    factory_related_name='customer',
  )
