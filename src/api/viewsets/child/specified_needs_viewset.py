from rest_framework import viewsets

from api.serializers.child.specified_needs_serializer import SpecifiedNeedsModelSerializer
from child.models.specified_needs_model import SpecifiedNeedsModel


class SpecifiedNeedsModelViewset(viewsets.ModelViewSet):
    queryset = SpecifiedNeedsModel.objects.all()
    serializer_class = SpecifiedNeedsModelSerializer