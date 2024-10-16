from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class PersonModel(NamedDateTimeModel):
    last_name = models.CharField(max_length=50)

    class Meta:
        abstract = True