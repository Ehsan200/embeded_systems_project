from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckAPIView(APIView):
    def post(self, request, *args, **kwargs):
        return Response(
            data=request.data,
            status=200,
        )
