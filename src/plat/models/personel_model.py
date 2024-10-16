from django.db import models
from base.models.person_model import PersonModel


class PersonelModel(PersonModel):
    enfant = models.ManyToManyField('child.ChildModel', related_name='enfant_personnel')
    matricule = models.CharField(max_length=100)