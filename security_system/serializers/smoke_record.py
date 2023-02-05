from rest_framework.serializers import ModelSerializer

from security_system.models import SmokeRecord


class SmokeRecordSerializer(ModelSerializer):
    class Meta:
        model = SmokeRecord
        fields = (
            'id',
            'time',
            'gas_type',
            'value',
            'raspberry',
        )

        extra_kwargs = {
            'raspberry': {'write_only': True}
        }
