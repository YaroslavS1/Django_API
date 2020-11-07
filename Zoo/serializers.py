from rest_framework import serializers

from .models import Animal, Place

class AnimalSerializer(serializers.Serializer):
    # created_at = serializers.DateTimeField()
    # update_at = serializers.DateTimeField()
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    age = serializers.FloatField()
    kind_animals_id = serializers.IntegerField()
    place_id = serializers.IntegerField()
    zookeeper_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.kind_animals_id = validated_data.get('kind_animals_id', instance.kind_animals_id)
        instance.place_id = validated_data.get('place_id', instance.place_id)
        instance.zookeeper_id = validated_data.get('zookeeper_id', instance.zookeeper_id)

    def create(self, validated_data):
        # print(**validated_data)
        return Animal.objects.create(**validated_data)

class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    # place_id = serializers.IntegerField()

class ZookeeperSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
