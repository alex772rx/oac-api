from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesViewSet

router = DefaultRouter()
router.register(r'sales', SalesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
