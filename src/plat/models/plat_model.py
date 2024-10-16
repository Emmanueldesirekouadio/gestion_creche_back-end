from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel


class PlatModel(NamedDateTimeModel):
    enfant = models.ManyToManyField('child.ChildModel', related_name='enfant_plat')
    type_plat = models.ForeignKey('plat.TypePlatModel', on_delete=models.CASCADE)
    personel = models.ForeignKey('plat.PersonelModel', on_delete=models.CASCADE)