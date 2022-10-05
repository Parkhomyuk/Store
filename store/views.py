from django.shortcuts import render
from rest_framework import generics, viewsets
 
from store.models import Brand, Category, Product, Subcategory



from store.serializers import BrandSerializer, CategorySerializer, ProductSerializer, SubcategorySerializer, SubcategoryWriteSerializer

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
class SubcategoryWriteDetail(generics.ListCreateAPIView):
    queryset=Subcategory.objects.all()
    serializer_class=SubcategoryWriteSerializer     

class CategoryList(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer 

class CategoryViewSet(viewsets.ModelViewSet):
        queryset=Category.objects.all()
        serializer_class=CategorySerializer 