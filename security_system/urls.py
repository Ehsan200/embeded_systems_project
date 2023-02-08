from django.urls import path
from rest_framework import routers

from security_system.views import ThiefRecordViewSet, SmokeRecordViewSet, HealthCheckAPIView, MotionRecordViewSet

router = routers.SimpleRouter()
router.register(r'smoke-records', SmokeRecordViewSet)
router.register(r'thief-records', ThiefRecordViewSet)
router.register(r'motion-records', MotionRecordViewSet)


urlpatterns = [
    *router.urls,
    path('health-check/', HealthCheckAPIView.as_view()),
]
