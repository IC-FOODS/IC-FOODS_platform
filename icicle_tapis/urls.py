from django.urls import path

from icicle_tapis.api import TapisCallbackAPI, TapisProtectedView


urlpatterns = [
    path(
        "callback/",
        TapisCallbackAPI.as_view(),
        name="callback",
    ),
    path(
        "protected/",
        TapisProtectedView.as_view(),
        name="protected",
    ),
]
