from rest_framework import serializers

from basic_app import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = "__all__"
