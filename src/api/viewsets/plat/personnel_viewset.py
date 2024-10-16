from rest_framework import viewsets

from api.serializers.plat.personnel_serializer import PersonnelModelSerializer
from plat.models.personel_model import PersonelModel


class PersonnelModelViewset(viewsets.ModelViewSet):
    queryset = PersonelModel.objects.all()
    serializer_class = PersonnelModelSerializer