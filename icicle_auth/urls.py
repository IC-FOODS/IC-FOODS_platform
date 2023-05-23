from django.urls import path
from knox.views import LogoutView

from icicle_auth.api import (
    SignUpAPI,
    LoginAPI,
    ActiveUserAPI,
)


urlpatterns = [
    path("register/", SignUpAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("active-user/", ActiveUserAPI.as_view()),
    path('logout/', LogoutView.as_view()),
]
