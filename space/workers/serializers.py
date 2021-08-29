from rest_framework import serializers
from .models import FieldWorker


class FieldWorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldWorker
        fields = '__all__'
        read_only_fields = ('create_at', 'id' )