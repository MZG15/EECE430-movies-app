from django.urls import include, path, re_path
from django.contrib import admin
urlpatterns = [
 path('vsapp/', include('vsapp.urls')),
 re_path('',include('vsapp.urls')),
]