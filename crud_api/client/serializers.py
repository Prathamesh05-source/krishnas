from rest_framework import serializers
from .models import Client
from django.contrib.auth.models import User


class ClientSerializer(serializers.ModelSerializer):  # create class to serializer model
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Client
        fields = ('id', 'name', 'created_by')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    clients = serializers.PrimaryKeyRelatedField(many=True, queryset=Client.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'created_at','created_by')
