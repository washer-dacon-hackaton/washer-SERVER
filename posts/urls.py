from django.urls import path
from django.conf import settings
from .views import PostCreateView
urlpatterns = [
    path('<str:nickname>/',PostCreateView.as_view(),name='PostCreate'),
]