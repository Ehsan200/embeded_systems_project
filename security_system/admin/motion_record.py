from django.contrib import admin
from ..models import MotionRecord


@admin.register(MotionRecord)
class MotionRecordAdmin(admin.ModelAdmin):
    readonly_fields = (
        'raspberry',
        'time',
    )

    list_display = (
        'id',
        'get_raspberry__ip',
        'time',
    )

    def get_raspberry__ip(self, obj):
        return obj.raspberry.ip

    get_raspberry__ip.short_description = 'raspberry__ip'
    get_raspberry__ip.admin_order_field = 'raspberry__ip'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(raspberry__admins__in=[request.user.id])
