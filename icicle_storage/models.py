from django.db import models

from icicle_base.models import UUIDBaseModel


class JSONObject(UUIDBaseModel):
    """
    JSON Object
    """
    title = models.CharField(max_length=128,blank=False,)
    owner = models.CharField(max_length=64,blank=False,)
    json_data = models.JSONField(blank=True,null=True,)
