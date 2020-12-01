from django.db import models

class Customer(models.Model):
  first_name = models.CharField(max_length = 200)
  last_name = models.CharField(max_length = 200)
  address_1 = models.CharField(max_length = 300)
  address_2 = models.CharField(max_length = 300)
  city = models.CharField(max_length = 200)
  state = models.CharField(max_length = 200)
  postal_code = models.CharField(max_length = 20)

  def __str__(self):
    return (self.first_name + " " + self.last_name)

class Subscription(models.Model):
  customer = models.ForeignKey(
    Customer,
    null=True,
    blank=True,
    on_delete=models.CASCADE
  )
  plan_name = models.CharField(max_length = 300)
  price = models.CharField(max_length = 20)

  def __str__(self):
    return self.plan_name

class Gift(models.Model):
  customer = models.ForeignKey(
    Customer,
    null=True,
    blank=True,
    on_delete=models.CASCADE
  )
  plan_name = models.CharField(max_length = 300)
  price = models.CharField(max_length = 20)
  recipient_email = models.CharField(max_length = 100)

  def __str__(self):
    return self.plan_name
