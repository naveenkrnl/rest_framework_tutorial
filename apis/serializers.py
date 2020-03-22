#import serializer from rest_framework
from rest_framework import serializers

class Geeks(object):
    def __init__(self, files, image):
        self.files = files
        self.image = image

# create a serializer
class GeeksSerializer(serializers.Serializer):
    # intialize fields
    files = serializers.FileField()
    image = serializers.ImageField()