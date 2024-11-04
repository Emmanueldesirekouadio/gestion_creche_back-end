from rest_framework import viewsets

from api.serializers.plat.type_plat_serializer import TypePlatModelSerializer
from plat.models.type_plat_model import TypePlatModel


class TypePlatModoelViewset(viewsets.ModelViewSet):
    queryset = TypePlatModel.objects.all()
    serializer_class = TypePlatModelSerializer