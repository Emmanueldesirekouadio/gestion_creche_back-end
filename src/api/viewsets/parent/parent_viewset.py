from rest_framework import viewsets
from api.serializers.parent.parent_serializer import ParentSerializer
from parent.models.parent_model import ParentModel



class ParentViewset(viewsets.ModelViewSet):
    queryset = ParentModel.objects.all()
    serializer_class = ParentSerializer