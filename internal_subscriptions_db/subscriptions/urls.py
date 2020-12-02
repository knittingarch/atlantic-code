from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'gifts', views.GiftViewSet)
router.register(r'subscriptions', views.SubscriptionViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
