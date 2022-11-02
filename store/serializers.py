from dataclasses import field
from itertools import product
from pyexpat import model
from rest_framework import serializers

from store.models import Brand, Category, Product, Subcategory

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Brand

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        fields=('name', 'description', 'feedbacks', 'feedbacks_count', 'images', 'price', 'rating', 'status', 'subcategory', 'characteristic', 'brand','created_at', 'updated_at')
        model=Product

class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields=('id','name', 'category')
        model= Subcategory

class CategorySerializer(serializers.ModelSerializer):
    #subcategories=SubcategorySerializer(many=True)
   # subcategories=serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    subcategories=SubcategorySerializer(many=True, read_only=False)
    class Meta:
      
        fields=('id','name','subcategories')
        model=Category
        