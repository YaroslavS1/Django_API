from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Count

from .models import Animal
from .models import Place
from .serializers import AnimalSerializer, PlaceSerializer


# Create your views here.
class AnimalView(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response({"animals": serializer.data})

    def post(self, request):
        animal = request.data.get('animal')
        # Create an article from the above data
        serializer = AnimalSerializer(data=animal)
        if  serializer.is_valid(raise_exception=True):
            animal_saved = serializer.save()
        return Response({"success": "Animal '{}' created successfully".format(animal_saved.name)})

# 1
# class PlaceView(APIView):
#     def get(self, request):
#         a = []
#         d = {}
#         plplace = Place.objects.all()
#         anplace = Animal.objects.all()
#         # serializer = PlaceSerializer(anplace, many=True)
#         # print(type(serializer))
#         anplace_ = anplace.values('place__name')
#         plplace_ = plplace.values('name')
#         for i in plplace_:
#             d.update({i['name']: ''})
#         for i in anplace_:
#             a.append(i['place__name'])
#         for k in d:
#             d[k] = a.count(k)
#         # print(d)
#         a.clear()
#         for k in d:
#             if d[k]>=2:
#                 a.append(k)
#         print(a)
#         serializer = PlaceSerializer({'name': a})
#         return Response(serializer.data)

class PlaceView(APIView):
    def get(self, request):


        a = Place.objects.filter(
            pk__in=Animal.objects.values('place').annotate(entries=Count('place')).filter(entries__gte=2).values(
                'place')).values('name')
        #print(list(a))
        serializer = PlaceSerializer(a, many=True)
        return Response(serializer.data)
