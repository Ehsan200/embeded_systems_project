from django.db import models


class BaseRecord(models.Model):
    raspberry = models.ForeignKey(
        to='security_system.Raspberry',
        on_delete=models.CASCADE,
    )

    time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
