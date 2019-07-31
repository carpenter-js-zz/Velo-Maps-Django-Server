from django.shortcuts import render
from rest_framework import status, generics, permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Route
from api.serializers import RouteSerializer, UserSerializer
from api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

# User views
class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# Route views

# Route List View
class RouteList(APIView):
  """
  List all routes, or create a new route.
  """
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

  def get(self, request, format=None):
      routes = Route.objects.all()
      serializer = RouteSerializer(routes, many=True)
      return Response(serializer.data)

  def post(self, request, format=None):
      serializer = RouteSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

# Route Detail View
class RouteDetail(APIView):
  """
  Retrieve, update or delete a route instance.
  """
  permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

  def get_object(self, pk):
    try:
        return Route.objects.get(pk=pk)
    except Route.DoesNotExist:
        raise Http404

  def get(self, request, pk, format=None):
    route = self.get_object(pk)
    serializer = RouteSerializer(route)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    route = self.get_object(pk)
    serializer = RouteSerializer(route, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    route = self.get_object(pk)
    route.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# function based views
#from rest_framework.decorators import api_view

# @api_view(['GET', 'POST'])
# def route_list(request, format=None):
#   """
#   List all routes, or create a new route.
#   """
#   if request.method == 'GET':
#     routes = Route.objects.all()
#     serializer = RouteSerializer(routes, many=True)
#     return Response(serializer.data)

#   elif request.method == 'POST':
#     serializer = RouteSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def route_detail(request, pk, format=None):
#   """
#   Retrieve, update or delete a route.
#   """
#   try:
#     route = Route.objects.get(pk=pk)
#   except Route.DoesNotExist:
#     return Response(status=status.HTTP_404_NOT_FOUND)
  
#   if request.method == 'GET':
#     serializer = RouteSerializer(route)
#     return Response(serializer.data)

#   ----TODO--- finishe PUT route name and description
#   elif request.method == 'PUT':
#     serializer = RouteSerializer(route, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   elif request.method == 'DELETE':
#     route.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)