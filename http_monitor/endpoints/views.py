from django.shortcuts import render

from .models import Endpoint

from rest_framework import (
    serializers,
    generics,
)
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
