from django.urls import path
from . import views

urlpatterns = [
    path('', views.ifscAPIView.as_view(), name="ifsc")
]