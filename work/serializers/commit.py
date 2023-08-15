from rest_framework import serializers
from ..models import Commit


class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Commit