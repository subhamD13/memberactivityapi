
from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
import uuid

class Timezone(models.Model):
    tz = models.CharField(max_length=60)

    def __str__(self):
        return self.tz


class Activity(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id} ({self.start_time} - {self.end_time})'


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    real_name = models.CharField(max_length=60)
    tz = models.ForeignKey(Timezone, on_delete=models.SET_NULL, null=True)
    activity_periods = models.ManyToManyField(Activity)

    def __str__(self):
        return str(self.real_name)
