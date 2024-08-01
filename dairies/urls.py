from django.urls import path
from django.conf import settings
from .views import DairyCreateView
urlpatterns = [
    path('<str:nickname>/',DairyCreateView.as_view(),name='DairyCreate'),
]