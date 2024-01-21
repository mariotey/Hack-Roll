from django.contrib.auth import authenticate, login, logout
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import User
import json
import requests
import ast

BOT_URL="https://hacknrollllm.onrender.com"

def index(request):
    return render(request, "timetable/home.html")

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

            return HttpResponseRedirect(reverse("timetable:index"))
        else:
            print("Login unsuccessful")
            return render(request, "timetable/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "timetable/login.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("timetable:index"))

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

            return HttpResponseRedirect(reverse("timetable:index"))

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

@login_required
def bot(request, scam_type):
    scam_info = json.loads(
        requests.post(f'{BOT_URL}/getInfo',
                        headers={"Content-Type": "application/json"},
                        json = {
                            "data": scam_type
                        }
        ).content.decode("utf-8")
    )

    linkValid = True
    while linkValid:
        quiz_info = json.loads(
            requests.post(f'{BOT_URL}/getScenarioQnAnswer',
                            headers={"Content-Type": "application/json"},
                            json = {
                                "data": scam_type
                            }
            ).content.decode("utf-8")
        )

        print(quiz_info,"\n")

        if "error" in quiz_info.keys():
            linkValid = True
        else:
            linkValid = False

    scenario_info = quiz_info["scenario"]



    question_info = {
        "question": quiz_info["question"],
        "answers": quiz_info["answers"],
        "correct": quiz_info["correct"],
        "answerContext": quiz_info["answerContext"],
    }

    return render(request, "timetable/bot.html", {
        "scam_type": scam_type,
        "scam_info": scam_info,
        "scenario_info": scenario_info,
        "question_info": question_info,
        "user_response": "",
        "respond_info": {"answer": ""}
    })

def respond(request, scam_type):
    if request.method == 'POST':
        # Extract the values from the form
        user_input = request.POST.get('user_input', '')
        js_variable_1 = ast.literal_eval(request.POST.get('js_variable_1', ''))
        js_variable_2 = ast.literal_eval(request.POST.get('js_variable_2', ''))
        js_variable_3 = ast.literal_eval(request.POST.get('js_variable_3', ''))

        respond_info = json.loads(
            requests.post(f'{BOT_URL}/replyUser',
                            headers={"Content-Type": "application/json"},
                            json = {
                                "data": user_input,
                                "context":js_variable_3["answerContext"]
                            }

            ).content.decode("utf-8")
        )

        print(respond_info)

        data = {
            "scam_type": scam_type,
            "scam_info": js_variable_1,
            "scenario_info": js_variable_2,
            "question_info": js_variable_3,
            "user_response": user_input,
            "respond_info": respond_info
        }

        return render(request, "timetable/bot.html", data)
