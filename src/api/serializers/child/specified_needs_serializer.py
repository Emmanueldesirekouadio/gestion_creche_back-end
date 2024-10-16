from rest_framework import serializers

from child.models.specified_needs_model import SpecifiedNeedsModel


class SpecifiedNeedsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecifiedNeedsModel
        fields = '__all__'