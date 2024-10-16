from rest_framework import serializers

from plat.models.menu_model import MenuModel


class MenuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'