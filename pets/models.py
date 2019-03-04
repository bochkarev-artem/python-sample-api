from django.db import models
from rest_framework import serializers, viewsets
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404


class Pets(models.Model):
    GENDER_CHOICES = (
        ('m', 'male'),
        ('w', 'female'),
    )

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "pets"

    def __str__(self):
        return self.name


class PetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pets
        fields = ('name', 'species', 'gender', 'birthday')


class PetsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing pets instances.
    """
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
    #
    # @staticmethod
    # def list_all():
    #     queryset = Pets.objects.all()
    #     serializer = PetsSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # @staticmethod
    # def get(pk=None):
    #     queryset = Pets.objects.all()
    #     pet = get_object_or_404(queryset, pk=pk)
    #     serializer = PetsSerializer(pet)
    #     return Response(serializer.data)
