from django.shortcuts import render, redirect
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .serializers import UserRegistrationSerializer, UserLoginSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])
            if user:
                login(request, user)  # Login the user and create a session
                return JsonResponse({
                    'user_id': user.id,
                    'email': user.email,
                    'message': 'Login successful'
                })
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)  # Login the user after registration
            return Response({
                'user_id': user.id,
                'email': user.email,
                'message': 'Registration successful and logged in'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterTemplateView(View):
    def get(self, request):
        return render(request, 'access/register.html')


class LoginTemplateView(View):
    def get(self, request):
        return render(request, 'access/login.html')
