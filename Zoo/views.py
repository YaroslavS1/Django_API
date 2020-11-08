from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Count
from django.utils import timezone

from .models import Animal, Place
from .serializers import AnimalSerializer, PlaceSerializer, ZookeeperSerializer, PlaceSortSerializer


# Create your views here.
class AnimalView(APIView):
    def get(self, request):
        name = request.query_params.get('name', '')
        animals = Animal.objects.get(name=name)
        serializer = AnimalSerializer(animals)
        return Response({"animals": serializer.data})

    def post(self, request):
        # Create an article from the above data
        name = request.data.get('name', '')
        age = request.data.get('age', '')
        kind_animals_id = request.data.get('kind_animals_id', '')
        place_id = request.data.get('place_id', '')
        zookeeper_id = request.data.get('zookeeper_id', '')
        animal = Animal.objects.create_user(name=name, age=age, kind_animals_id=kind_animals_id, place_id=place_id,
                                            zookeeper_id=zookeeper_id)
        animal.save()
        return Response({"status": 'ok'})

    def put(self, request):
        name = request.data.get('name', '')
        new_zookeper_id = request.data.get('old_zookeper_id', '')
        animal = Animal.objects.get(name=name)
        if not animal:
            return Response({'status': 'fail'})
        animal.zookeeper_id = new_zookeper_id
        return Response({'ststus':'ok'})


    def delete(self, request):
        animal = Animal.objects.get('name')
        name = request.qwery_params.get('name', '')
        animal.objects.get(name=name).delete()
        return Response({'ststus': 'ok'})


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
        # print(list(a))
        serializer = PlaceSerializer(a, many=True)
        return Response(serializer.data)


class ZookeeperView(APIView):
    def get(self, request):
        one_year_earlier = timezone.now() - timezone.timedelta(days=365)
        print(one_year_earlier)
        date = Animal.objects.filter(zookeeper_date_set__lt=one_year_earlier)
        serializer = ZookeeperSerializer(date, many=True)
        return Response(serializer.data)
    # def


class PlaceSortView(APIView):
    # serializer = PlaceSortZookeeperSerializer
    def get(self, request):
        # print(request)
        square = request.GET.get('square')
        temperature = request.GET.get('temperature')
        lighting = request.GET.get('lighting')
        place = Animal.objects.filter(
            place__name__in=Place.objects.filter(square=square, temperature=temperature, lighting=lighting).values_list(
                'name', flat=True))
        serializer = PlaceSortSerializer(place, many=True)
        return Response(serializer.data)

# http://127.0.0.1:8000/api/placesort/?square=2&temperature=2&lighting=False
