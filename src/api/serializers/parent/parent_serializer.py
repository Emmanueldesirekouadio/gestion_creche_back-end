from rest_framework import serializers
from parent.models.parent_model import ParentModel


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentModel
        fields = '__all__'