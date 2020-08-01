
from rest_framework import viewsets

from .serializers import ActivitySerializer, TimezoneSerializer, UserSerializer
from .models import Activity, User, Timezone

class TimezoneView(viewsets.ModelViewSet):
    queryset = Timezone.objects.all()
    serializer_class = TimezoneSerializer

class ActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
