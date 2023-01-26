from django.db import models

from endpoints.models import Endpoint



# Create your models here.

class healthCheckRequest(models.Model):
    endpoint = models.ForeignKey(
        Endpoint,
        on_delete=models.CASCADE,
        related_name='requests',
        blank=False,
        null=False,
    )
    status = models.CharField(max_length=10)
    sends_at = models.DateTimeField()
