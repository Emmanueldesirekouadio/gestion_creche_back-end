from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class AllergiesModel(NamedDateTimeModel):
    enfant = models.ForeignKey('child.ChildModel', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=180)