from rest_framework import serializers

class ShapeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    fa_class = serializers.CharField(max_length=200)

class ColorSchemeSerilizer(serializers.Serializer):
    color1 = serializers.CharField(max_length=40)
    color2 = serializers.CharField(max_length=40)
    color3 = serializers.CharField(max_length=40)
    color4 = serializers.CharField(max_length=40)
