from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('add_video/',views.add_video, name='add_video'),
 path('display_video/',views.display_video, name='display_video'),
 path('delete_video/', views.delete_video, name='delete_video'),
 path('update_video/', views.update_video, name='update_video'),
]