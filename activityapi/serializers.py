from rest_framework import serializers
from .models import Activity, Timezone, User

class TimezoneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Timezone
        fields = ('url', 'tz')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    start_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")
    end_time = serializers.DateTimeField(format="%b %d %Y %I:%M%p")
    class Meta:
        model = Activity
        fields = ('url', 'start_time', 'end_time')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    activity_periods = ActivitySerializer(read_only=True, many=True)
    # tz = TimezoneSerializer(read_only=True)
    tz = serializers.SerializerMethodField('get_timezone')
    class Meta:
        model = User
        fields = ('url', 'id', 'real_name', 'tz', 'activity_periods')

    def get_timezone(self, user):
        tzo = user.tz.tz
        return tzo
    