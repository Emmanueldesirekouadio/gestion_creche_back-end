from rest_framework import viewsets

from api.serializers.parent.user_role_serializer import UserRoleModelSerializer
from parent.models.user_role_model import UserRoleModel


class UserRoleModelViewset(viewsets.ModelViewSet):
    serializer_class = UserRoleModelSerializer
    queryset = UserRoleModel.objects.all()