from django.shortcuts import render
from .models import User
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password

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
def login(request):
    if request.method == 'POST':
        print("IN LOGIN POST BODY")
        data = json.loads(request.body)
        print("Received data:", data)
        response_data = {'message' : 'Data received successfully!', 'receivedData': data}
        return JsonResponse(response_data, status=200)
    return HttpResponse('login')
