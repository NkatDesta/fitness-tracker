from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/template/", views.login_template_view, name="login_template"),
    path("register/template/", views.register_template_view, name="register_template"),
    path("logout/", views.logout_view, name="logout"),
]
