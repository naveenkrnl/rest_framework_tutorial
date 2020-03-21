#import serializer from rest_framework
from rest_framework import serializers

class Geeks(object):
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

# create a serializer
class GeeksSerializer(serializers.Serializer):
    # intialize fields
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()
    phone_number = serializers.RegexField("[0-9]{10}")