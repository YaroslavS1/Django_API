from django.db import models
from django.utils import timezone


# Create your models here.
class Animal(models.Model):
    created_at = models.DateTimeField(editable=False)
    update_at = models.DateTimeField(editable=False)
    name = models.CharField(max_length=20)
    age = models.FloatField(default=0)
    kind_animals = models.ForeignKey('Kind_animal', related_name='Zoo', null=True, blank=True,
                                     on_delete=models.SET_NULL)
    place = models.ForeignKey('Place', related_name='Zoo', null=True, on_delete=models.SET_NULL)

    zookeeper = models.ForeignKey('Zookeeper', related_name='Zoo', null=True, on_delete=models.SET_NULL)
    zookeeper_date_set = models.DateTimeField(default=0, editable=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        else:
            old = type(self).objects.get(pk=self.pk) if self.pk else None
            super(Animal, self).save(*args, **kwargs)
            if old.zookeeper != self.zookeeper:  # Field has changed
                self.zookeeper_date_set = timezone.now()
        self.update_at = timezone.now()
        return super(Animal, self).save(*args, **kwargs)


class Kind_animal(models.Model):
    created_at = models.DateTimeField(editable=False)
    update_at = models.DateTimeField(editable=False)
    name = models.CharField(max_length=20)
    character = models.CharField(max_length=50, default='')
    diet = models.CharField(max_length=100, default='')
    lifespan = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.update_at = timezone.now()
        return super(Kind_animal, self).save(*args, **kwargs)


class Place(models.Model):
    created_at = models.DateTimeField(editable=False)
    update_at = models.DateTimeField(editable=False)
    name = models.CharField(max_length=20)
    square = models.FloatField(default=0.0)
    temperature = models.FloatField(default=0.0)
    lighting = models.BooleanField()

    # animals = Animal._meta.get_field('place').related_model

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.update_at = timezone.now()
        return super(Place, self).save(*args, **kwargs)


class Zookeeper(models.Model):
    created_at = models.DateTimeField(editable=False)
    update_at = models.DateTimeField(editable=False)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    MAN = 'МУЖ'
    FEMALE = 'ЖЕН'
    GENDER = (
        (MAN, 'Мужчина'),
        (FEMALE, 'Женщина'),
    )
    gender = models.CharField(max_length=3, choices=GENDER, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.update_at = timezone.now()
        return super(Zookeeper, self).save(*args, **kwargs)
