from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
  path('api/', views.route_list),
  path('api/<int:pk>/', views.route_detail),
]

# Adds format suffixes to API endpoints
urlpatterns = format_suffix_patterns(urlpatterns)