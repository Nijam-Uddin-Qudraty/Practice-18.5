
from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name="homepage"),
    path("signup", views.register, name="signup"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("profile", views.profile, name="profile"),
    path("profile/pass1", views.pass_with, name="pass1"),
    path("profile/pass2", views.pass_without, name="pass2"),

]

