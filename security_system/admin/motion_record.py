from django.contrib import admin
from ..models import MotionRecord


@admin.register(MotionRecord)
class SmokeRecordAdmin(admin.ModelAdmin):
    readonly_fields = (
        'raspberry',
        'time',
    )

    list_display = (
        'id',
        'raspberry__ip',
        'time',
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(raspberry__admins__in=[request.user.id])
