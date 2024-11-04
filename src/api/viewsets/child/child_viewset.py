from rest_framework import viewsets

from api.serializers.child.child_serializer import ChildModelSerializer
from child.models.child_model import ChildModel


class ChildModelViewset(viewsets.ModelViewSet):
    queryset = ChildModel.objects.all()
    serializer_class = ChildModelSerializer