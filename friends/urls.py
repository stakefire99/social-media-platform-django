from django.urls import path
from . import views

urlpatterns = [
    path('', views.friend_list, name='friend-list'),
    path('send/<str:username>/', views.send_request, name='send-request'),
    path('accept/<int:pk>/', views.accept_request, name='accept-request'),
]