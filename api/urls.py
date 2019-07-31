from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
  path('api/', views.RouteList.as_view()),
  path('api/<int:pk>/', views.RouteDetail.as_view()),
  path('users/', views.UserList.as_view()),
  path('users/<int:pk>/', views.UserDetail.as_view()),

]

# Adds format suffixes to API endpoints
urlpatterns = format_suffix_patterns(urlpatterns)

# adds login and logout to browsable api
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]