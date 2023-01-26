from django.http import JsonResponse

from .models import Endpoint

from rest_framework import (
    serializers,
    generics,
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class EndpointSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.URLField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    threshold = serializers.IntegerField()
    class Meta:
        model = Endpoint
        fields = ('id', 'url', "user" ,'threshold')


class CreateNewEndpoint(generics.CreateAPIView):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()
    permission_classes = [IsAuthenticated,]


class DeleteEndpoint(generics.DestroyAPIView):
    serializers = EndpointSerializer
    queryset = Endpoint.objects.all()
    permission_classes = [IsAuthenticated,]


class GetEndpointId(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        endpoint_url = request.data['url']
        try:
            endpoint_id = Endpoint.objects.get(url=endpoint_url, user=request.user).id
            return JsonResponse({'id': endpoint_id})
        except:
            return JsonResponse({'error': 'you have not added this url'})
