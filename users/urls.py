from django.urls import path, include
from .views import AuthAPIView

urlpatterns = [
    path('oauth', AuthAPIView.as_view()),
]