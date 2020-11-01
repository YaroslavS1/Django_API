from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Animal

# Create your views here.
class AnimalView(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        return Response({"animals": animals})