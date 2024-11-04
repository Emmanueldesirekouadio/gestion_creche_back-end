from rest_framework import serializers
from parent.models.user_role_model import UserRoleModel


class UserRoleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoleModel
        fields = '__all__'