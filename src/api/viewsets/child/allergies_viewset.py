from rest_framework import viewsets

from api.serializers.child.allergies_serializer import AllergiesModelSerializer
from child.models.allergie_model import AllergiesModel


class AllergiesModelViewset(viewsets.ModelViewSet):
    queryset = AllergiesModel.objects.all()
    serializer_class = AllergiesModelSerializer