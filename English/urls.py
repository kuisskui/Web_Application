from django.urls import path
from . import views


app_name = "English"
urlpatterns = [
    path("", views.home, name="home"),
]
