from dataclasses import field, fields
from itertools import product
from pyexpat import model
from rest_framework import serializers

from store.models import Brand, Category, Product, Subcategory

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Brand

class ProductSerializer(serializers.ModelSerializer):
    #brand=serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    class Meta: 
       # fields=('name', 'description', 'feedbacks', 'feedbacks_count', 'images', 'price', 'rating', 'status', 'subcategory', 'characteristic', 'brand','created_at', 'updated_at')
        fields='__all__'
        model=Product
        depth = 2

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model= Subcategory
        depth=1
class SubcategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model= Subcategory
                

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields=('name'),
        model=Category