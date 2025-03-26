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
        print("IN POST BODY")
        data = json.loads(request.body)
        print('Received data:', data)
        response_data = {'message': 'Data received successfully!', 'receivedData': data}
        print("Adding user to database")
        User.objects.create(
            username= data.get('username'),
            password = make_password(data.get('password')),
            fullname = data.get('fullName'),
            email = data.get('email')
        )
        return JsonResponse(response_data, status=200)
    return HttpResponse('signup')

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        print("IN LOGIN POST BODY")
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print("USEr",user)
        if user is not None:
            login(request, user)
            response = JsonResponse({'message': 'login successful'}, status=200)
            response.set_cookie('sessionid', request.session.session_key, httponly=True, samesite='Lax')
            return response
        else:
            return JsonResponse({'message': 'Login failure'}, status=401)

@csrf_exempt
def user_logout(request):
    logout(request)
    return JsonResponse({'message' : 'logout succesful'}, status=200)


@login_required
def check_authentication(request):
    serializer = UserSerializer(request.user)
    return JsonResponse({'authenticated': True, 'user': serializer.data})

@csrf_exempt
def not_authenticated(request):
    return JsonResponse({'authenticated': False})
