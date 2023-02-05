from django.db import models

from security_system.models import BaseRecord


class SmokeRecord(BaseRecord):
    smoke = models.FloatField()

    methan = models.FloatField()

    lpg = models.FloatField()

    hydrogen = models.FloatField()
