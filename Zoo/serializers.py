from rest_framework import serializers

class AnimalSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()
    name = serializers.CharField(max_length=20)
    # title = serializers.CharField(max_length=120)
    # description = serializers.CharField()
    # body = serializers.CharField()