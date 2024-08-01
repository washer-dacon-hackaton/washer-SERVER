from django.urls import path
from django.conf import settings
from .views import LoginView
urlpatterns = [
    path('login/',LoginView.as_view(),name='Login'),
]