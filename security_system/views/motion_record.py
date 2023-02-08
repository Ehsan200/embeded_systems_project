from rest_framework.viewsets import ModelViewSet

from security_system.models import MotionRecord
from security_system.serializers.motion_record import MotionRecordSerializer


class MotionRecordViewSet(ModelViewSet):
    queryset = MotionRecord.objects.all()
    serializer_class = MotionRecordSerializer
