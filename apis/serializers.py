#import serializer from rest_framework
from rest_framework import serializers

class Geeks(object):
    def __init__(self, URL, slug):
        self.URL = URL
        self.slug = slug

# create a serializer
class GeeksSerializer(serializers.Serializer):
    # intialize fields
    URL = serializers.URLField()
    slug = serializers.SlugField()
