from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q

from .models import User
from datetime import datetime, timedelta
import json

def index(request):
    return render(request, "timetable/login.html")

#################################################################################################

def login_user(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            print("Login successful")

            return render(request, "timetable/menu.html")
        else:
            print("Login unsuccessful")
            return render(request, "timetable/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "timetable/login.html")

def logout_user(request):
    logout(request)
    return render(request, "timetable/login.html")

def register(request):
    print(request)

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        print(username)

        if password != confirmation:
            return render(request, "timetable/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)

            login(request, user)

            return render(request, "timetable/menu.html")

        except IntegrityError:
            return render(request, "timetable/register.html", {
                "message": "Username or email already taken."
            })

        except Exception as error:
            print(error)

    else:
        return render(request, "timetable/register.html")

#################################################################################################

@login_required  # Add the login_required decorator to ensure the user is authenticated
def menu(request):
    return render(request, "timetable/menu.html")
