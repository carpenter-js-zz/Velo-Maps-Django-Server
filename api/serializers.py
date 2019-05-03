from rest_framework import serializers
from api.models import Route

# ModelSerializer sets up a basic serializer with create and update methods
class RouteSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Route
    fields = ('id', 'name', 'path', 'description')

    # add validators