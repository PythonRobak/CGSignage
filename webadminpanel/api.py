from rest_framework import viewsets, permissions
from webadminpanel.models import User
from webadminpanel.serializers import UsersSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    # permission_classes = (permissions.IsAuthenticated)
