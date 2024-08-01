from django.urls import path
from django.conf import settings
from .views import ReportView
urlpatterns = [
    path('<str:nickname>/',ReportView.as_view(),name=''),
]

