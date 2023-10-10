from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('chatbot', views.chatbot, name='chatbot'),
    path('logout', views.logout, name='logout'),
]