from rest_framework import serializers
from child.models.activity_model import ActivityModel


class ActivityModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityModel
        fields = '__all__'