from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class UserRoleModel(DateTimeModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name