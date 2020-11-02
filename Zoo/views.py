from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Animal
from .serializers import AnimalSerializer

# Create your views here.
class AnimalView(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response({"animals": serializer.data})

    def post(self, request):
        animal = request.data.get('Animal')
        # Create an article from the above data
        serializer = AnimalSerializer(data=animal)
        if serializer.is_valid(raise_exception=True):
            animal_saved = serializer.save()
        return Response({"success": "Animal '{}' created successfully".format(animal_saved.title)})