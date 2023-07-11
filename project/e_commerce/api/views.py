from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from .models import User

class UserRegistrationAPIView(APIView):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            if user.userType == 'admin':
                all_users = User.objects.all()
                all_users_serializer = UserSerializer(all_users, many=True)
                return render(request, 'adminView.html', {'users': all_users_serializer.data})
            serializer = UserSerializer(user)
            return render(request, 'customerView.html', {'user': serializer.data})
        except User.DoesNotExist:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutAPIView(APIView):

    def post(self, request):
        return redirect('login')
