#import serializer from rest_framework
from rest_framework import serializers

# create a serializer
class CommentSerializer(serializers.Serializer):
    # intialize fields
    field_1 = serializers.BooleanField()
    field_2 = serializers.NullBooleanField()