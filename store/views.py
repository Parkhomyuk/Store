from django.shortcuts import render
from rest_framework import generics
from store.models import Brand, Category, Product, Subcategory



from store.serializers import BrandSerializer, CategorySerializer, ProductSerializer, SubcategorySerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

class BrandList(generics.ListCreateAPIView):
    queryset=Brand.objects.all()   
    serializer_class=BrandSerializer 

class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Brand.objects.all()   
    serializer_class=BrandSerializer     

class SubcategoryList(generics.ListCreateAPIView):
    queryset=Subcategory.objects.all()
    serializer_class=SubcategorySerializer

class SubcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Subcategory.objects.all()
    serializer_class=SubcategorySerializer    

class CategoryList(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer 