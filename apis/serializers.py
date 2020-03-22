#import serializer from rest_framework
from rest_framework import serializers

class Geeks(object):
    def __init__(self, date_time, date, time, duration):
        self.date_time = date_time
        self.date = date
        self.time = time
        self.duration = duration

# create a serializer
class GeeksSerializer(serializers.Serializer):
    # intialize fields
    date_time = serializers.DateTimeField()
    date = serializers.DateField()
    time = serializers.TimeField()
    duration = serializers.DurationField()