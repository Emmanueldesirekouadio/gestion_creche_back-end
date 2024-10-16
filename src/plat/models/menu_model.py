from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class MenuModel(DateTimeModel):
    plat = models.ForeignKey('plat.PlatModel', on_delete=models.CASCADE)