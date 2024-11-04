from rest_framework import viewsets

from api.serializers.plat.plat_serializer import PlatModelSerialier
from plat.models.plat_model import PlatModel


class PlatModelViewset(viewsets.ModelViewSet):
    queryset = PlatModel.objects.all()
    serializer_class = PlatModelSerialier