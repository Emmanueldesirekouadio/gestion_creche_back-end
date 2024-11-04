from django.db import models
from base.models.person_model import PersonModel


class ChildModel(PersonModel):
    parent = models.ForeignKey('parent.ParentModel', on_delete=models.CASCADE)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name}"