from django.urls import path

from icicle_tapis.api import TapisLoginAPI, TapisUserInfoAPI


urlpatterns = [
    path("login/", TapisLoginAPI.as_view()),
    path(
        "user-info/",
        TapisUserInfoAPI.as_view(),
        name="user-info",
    ),
]
