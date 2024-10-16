from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class SpecifiedNeedsModel(DateTimeModel):
    enfant = models.ForeignKey('child.ChildModel', on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=180)