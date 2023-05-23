from django.urls import path

from icicle_tapis.api import TapisLoginAPI


urlpatterns = [
    path("login/", TapisLoginAPI.as_view()),
]
