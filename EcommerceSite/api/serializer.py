from rest_framework import serializers
from CommerceAdmin.models import *


class  productSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Product
        fields = [
                     'id',
                     'title',
                     'Price',
                     'description',
                     'Brand',
                     'tags',
                     'sizes',
                     'colors',
                     'Stock',
                     'category',
                 ]


class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = [
                     'Name',
                     'Picture',
                     'Active'
                 ]
