from django.urls import path
from . import views

app_name = "timetable"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register, name="register"),

    path("menu", views.menu, name="menu"),

    path('bot/<int:scam_id>/', views.bot, name='bot'),
    path("respond/<int:scam_id>/", views.respond, name="respond")
]
