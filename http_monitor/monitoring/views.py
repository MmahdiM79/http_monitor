from datetime import datetime
from datetime import timedelta

from django.http import JsonResponse

from .models import healthCheckRequest
from endpoints.models import Endpoint

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class GetWarnings(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        duration_hours = int(request.data['duration_hours'])
        requests_from_time = datetime.now() - timedelta(hours=duration_hours)
        endpoints_of_user = Endpoint.objects.filter(user=request.user)
        result = {}
        for endpoint in endpoints_of_user:
            requests_of_endpoint = healthCheckRequest.objects.filter(
                endpoint=endpoint,
                sends_at__gt=requests_from_time
            )
            result[str(endpoint.url)] = {
                'number_of_success': 0,
                'number_of_failures': 0,
                'threshold': endpoint.threshold,
                'state': None,
            }
            for request in requests_of_endpoint:
                if request.status == 'OK':
                    result[str(endpoint.url)]['number_of_success'] += 1
                else:
                    result[str(endpoint.url)]['number_of_failures'] += 1
            if result[str(endpoint.url)]['number_of_failures'] > endpoint.threshold:
                result[str(endpoint.url)]['state'] = 'unhealthy'
            else:
                result[str(endpoint.url)]['state'] = 'healthy'

        return JsonResponse(data=result)
