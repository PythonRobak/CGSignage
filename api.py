from rest_framework import routers
from webadminpanel.api import UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
