from django.db import models
from base.models.helpers.date_time_model import DateTimeModel


class UserModel(DateTimeModel):
    user_role = models.ForeignKey('parent.UserRoleModel', on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.username}"