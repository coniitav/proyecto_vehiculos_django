from django.urls import path
from .views import index, add

urlpatterns = [
    path("", index, name="index"),
    path("add", add, name="add"),
]