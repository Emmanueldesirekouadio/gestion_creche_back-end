from django.db import models
from base.models.person_model import PersonModel


class ParentModel(PersonModel):
    user = models.OneToOneField('parent.UserModel', on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    link = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.last_name} {self.name}"