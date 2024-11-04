from rest_framework import serializers
from child.models.allergie_model import AllergiesModel


class AllergiesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllergiesModel
        fields = '__all__'