from rest_framework.serializers import ModelSerializer

from security_system.models import MotionRecord


class MotionRecordSerializer(ModelSerializer):
    class Meta:
        model = MotionRecord
        fields = (
            'id',
            'raspberry',
        )

        extra_kwargs = {
            'raspberry': {'write_only': True}
        }
