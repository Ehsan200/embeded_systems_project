from rest_framework.viewsets import ModelViewSet

from security_system.models import ThiefRecord
from security_system.serializers import ThiefRecordSerializer


class ThiefRecordViewSet(ModelViewSet):
    queryset = ThiefRecord.objects.all()
    serializer_class = ThiefRecordSerializer
