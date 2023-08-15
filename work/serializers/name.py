from rest_framework import serializers
from ..models import Name


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Name