import requests
import time
from datetime import datetime

from django.core.management.base import BaseCommand

from endpoints.models import Endpoint
from monitoring.models import healthCheckRequest


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'time_interval',
            type=int,
            default=1
        )

    @staticmethod
    def health_checker() -> None:
        endpoints = Endpoint.objects.all()
        for endpoint in endpoints:
            print(f"\nChecking {endpoint.url} for {endpoint.user} ...\n")
            try:
                response = requests.get(endpoint.url, verify=False, timeout=10)
                healthCheckRequest.objects.create(
                    endpoint=endpoint,
                    status= "OK" if response.status_code//100 == 2 else "Failed",
                )
            except:
                healthCheckRequest.objects.create(
                    endpoint=endpoint,
                    status="Failed",
                )

    def handle(self, *args, **options):
        time_interval = options['time_interval']
        while True:
            Command.health_checker()
            time.sleep(time_interval)
