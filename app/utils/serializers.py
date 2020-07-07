from rest_framework import serializers
from core.models import Util


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Util
        fields = ('id', 'type', 'value')
