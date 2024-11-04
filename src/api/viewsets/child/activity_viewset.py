from rest_framework import viewsets

from api.serializers.child.activity_serializer import ActivityModelSerializer
from child.models.activity_model import ActivityModel


class ActivityModelViewset(viewsets.ModelViewSet):
    queryset = ActivityModel.objects.all()
    serializer_class = ActivityModelSerializer