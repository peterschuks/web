from django.db import models
from accounts.models import account

class UserLocation(models.Model):
    user = models.OneToOneField(account, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.latitude}, {self.longitude}"

