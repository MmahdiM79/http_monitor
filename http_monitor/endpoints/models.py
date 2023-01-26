from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Endpoint(models.Model):
    url = models.URLField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='endpoints'
    )
    threshold = models.IntegerField()   
