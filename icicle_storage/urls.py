from django.urls import path

from icicle_storage.api import (
    JSONObjectListAPI,
    JSONObjectCreateAPI,
    JSONObjectViewAPI,
)


urlpatterns = [
    path("json-object/create/", JSONObjectCreateAPI.as_view()),
    path("json-objects/", JSONObjectListAPI.as_view()),
    path("json-object/<uuid:uuid>/", JSONObjectViewAPI.as_view()),
]
