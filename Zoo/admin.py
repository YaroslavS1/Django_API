from django.contrib import admin
from .models import Animal, Kind_animal, Place, Zookeeper

# Register your models here.

admin.site.register(Animal)
admin.site.register(Kind_animal)
admin.site.register(Place)
admin.site.register(Zookeeper)

