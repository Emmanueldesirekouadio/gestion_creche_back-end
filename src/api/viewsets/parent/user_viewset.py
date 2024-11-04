from rest_framework import viewsets
from api.serializers.parent.user_serializer import UserModelSerializer
from parent.models.user_model import UserModel


class UserModelViewset(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = UserModel.objects.all()