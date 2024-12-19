from django.urls import path
from .views import index, add, sign_up, sign_up_create, sign_in, sign_out, listar

urlpatterns = [
    path("", index, name="index"),
    path("add", add, name="add"),
    path("sign_up", sign_up, name="sign_up"),
    path("sign_up/create", sign_up_create, name="sign_up_create"),
    path("sign_in", sign_in, name="sign_in"),
    path("sign_out", sign_out, name="sign_out"),
    path("listar", listar, name="listar"),
]