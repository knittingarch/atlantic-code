from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, basename='customer')
router.register(r'gifts', views.GiftViewSet, basename='gift')
router.register(r'subscriptions', views.SubscriptionViewSet, basename='subscription')

urlpatterns = [
  path('', include(router.urls)),
]
