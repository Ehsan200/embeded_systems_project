from rest_framework.viewsets import ModelViewSet

from security_system.models import SmokeRecord
from security_system.serializers import SmokeRecordSerializer


class SmokeRecordViewSet(ModelViewSet):
    queryset = SmokeRecord.objects.all()
    serializer_class = SmokeRecordSerializer
