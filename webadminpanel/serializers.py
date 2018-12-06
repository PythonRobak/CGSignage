from django.contrib.auth.models import User
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']


