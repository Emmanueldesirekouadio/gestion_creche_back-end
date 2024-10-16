from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class ActivityModel(NamedDateTimeModel):
    enfant = models.ManyToManyField('child.ChildModel', related_name='enfant_activities')
    description = models.CharField(max_length=180)
    duration = models.IntegerField()