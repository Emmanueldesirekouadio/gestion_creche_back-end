from rest_framework import serializers

from plat.models.plat_model import PlatModel


class PlatModelSerialier(serializers.ModelSerializer):
    class Meta:
        model = PlatModel
        fields = '__all__'