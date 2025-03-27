from django.shortcuts import render
from .models import User, Pokemon
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .serializers import UserSerializer, PokemonSerializer


@api_view(['GET'])
def get_pokemon(request):
    pokemon = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemon, many = True)
    return Response(serializer.data)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            print("IN POST BODY")
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            full_name = data.get('fullName')
            email = data.get('email')

            if User.objects.filter(username = username).exists():
                return JsonResponse({'error': 'Username already exists!'}, status = 400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists!'}, status=400)

            User.objects.create(
                username= data.get('username'),
                password = make_password(data.get('password')),
                fullname = data.get('fullName'),
                email = data.get('email')
            )
            return JsonResponse({'message:': 'User registered successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return HttpResponse('invalid request method', status=405)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = JsonResponse({'message': 'login successful'}, status=200)
                response.set_cookie('sessionid', request.session.session_key, httponly=True, samesite='Lax')
                return response
            else:
                return JsonResponse({'error': 'Invalid username or password'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return HttpResponse('Invalid request method', status=405)

@csrf_exempt
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        response = JsonResponse({'message': 'Logout successful'})
        response.delete_cookie('sessionid')
        response.delete_cookie('csrftoken')
        return response
    else:
        return JsonResponse({'message': 'User not authenticated'}, status=401)


@login_required
def check_authentication(request):
    serializer = UserSerializer(request.user)
    return JsonResponse({'authenticated': True, 'user': serializer.data})

@csrf_exempt
def not_authenticated(request):
    return JsonResponse({'authenticated': False})
