#import serializer from rest_framework
from rest_framework import serializers

class Geeks(object):
    def __init__(self, name,hidden):
        self.name = name
        self.hidden = hidden

# create a serializer
class GeeksSerializer(serializers.Serializer):
    # intialize fields
    name = serializers.CharField()
    hidden = serializers.HiddenField(default = 1)