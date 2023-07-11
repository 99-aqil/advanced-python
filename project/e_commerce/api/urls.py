from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
]