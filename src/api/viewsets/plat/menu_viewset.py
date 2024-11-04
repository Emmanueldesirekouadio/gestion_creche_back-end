from rest_framework import viewsets

from api.serializers.plat.menu_serializer import MenuModelSerializer
from plat.models.menu_model import MenuModel


class MenuModelViewset(viewsets.ModelViewSet):
    queryset = MenuModel.objects.all()
    serializer_class = MenuModelSerializer