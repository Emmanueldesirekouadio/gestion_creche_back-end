from rest_framework import serializers
from child.models.child_model import ChildModel


class ChildModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildModel
        fields = '__all__'