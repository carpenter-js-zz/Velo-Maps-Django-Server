from rest_framework import serializers
from api.models import Route
from django.contrib.auth.models import User

# Using django's user model
class UserSerializer(serializers.ModelSerializer):
    routes = serializers.PrimaryKeyRelatedField(many=True, queryset=Route.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'routes')

# ModelSerializer sets up a basic serializer with create and update methods
class RouteSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta: 
    model = Route
    fields = ('id', 'name', 'path', 'description', 'owner')

    # add validators