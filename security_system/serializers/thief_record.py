from rest_framework.serializers import ModelSerializer

from security_system.models import ThiefRecord


class ThiefRecordSerializer(ModelSerializer):
    class Meta:
        model = ThiefRecord
        fields = (
            'id',
            'time',
            'image',
            'raspberry',
        )

        extra_kwargs = {
            'raspberry': {'write_only': True}
        }
