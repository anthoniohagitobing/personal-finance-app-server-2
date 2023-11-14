from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import User
import json

# Create your views here.
def home(request):
    return HttpResponse("Test backend server")

def get_user(request, email):
    # Query using data
    data = User.objects.filter(email=email).values()
    # print(email)
    # print(data)

    # http://localhost:8080/rest/user/user1@gmail.com/
    return HttpResponse(data, status=200)

def create_user(request):
    print(request.method)
    # Processing incoming data
    data = json.loads(request.body)
        # json.loads already convert JSON string into python object 
    # User.objects.create(
    #     email = data['email'],
    #     first_name = data['firstName'],
    #     last_name = data['lastName'],
    # )
    # print(data['email'])
    return HttpResponse("User created in backend database", status=201)