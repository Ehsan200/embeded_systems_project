from django.db import models

from security_system.models import BaseRecord


class SmokeRecord(BaseRecord):
    gas_type = models.CharField(max_length=250)

    value = models.FloatField()
