#import serializer from rest_framework
from rest_framework import serializers

class Geeks(object):
    def __init__(self, ip):
        self.ip = ip

# create a serializer
class GeeksSerializer(serializers.Serializer):
    # intialize fields
    ip = serializers.IPAddressField()
