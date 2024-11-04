from rest_framework import serializers

from plat.models.personel_model import PersonelModel


class PersonnelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonelModel
        fields = '__all__'