from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Route
from api.serializers import RouteSerializer

@api_view(['GET', 'POST'])
def route_list(request, format=None):
  """
  List all routes, or create a new route.
  """
  if request.method == 'GET':
    routes = Route.objects.all()
    serializer = RouteSerializer(routes, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = RouteSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def route_detail(request, pk, format=None):
  """
  Retrieve, update or delete a route.
  """
  try:
    route = Route.objects.get(pk=pk)
  except Route.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = RouteSerializer(route)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = RouteSerializer(route, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    route.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)