from rest_framework import serializers

from plat.models.type_plat_model import TypePlatModel


class TypePlatModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePlatModel
        fields = '__all__'