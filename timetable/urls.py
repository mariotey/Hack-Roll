from django.urls import path
from . import views

app_name = "timetable"

urlpatterns = [
    path("", views.index, name="index"),
    path("homefalse", views.home_false, name="homefalse"),
    path("hometrue", views.home_true, name="hometrue"),

    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register, name="register"),

    path("menu", views.menu, name="menu"),

    path('bot/<str:scam_type>/', views.bot, name='bot'),
    path("respond/<str:scam_type>/", views.respond, name="respond"),
]
