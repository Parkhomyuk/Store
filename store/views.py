from django.shortcuts import render
from rest_framework import generics, viewsets
from django_filters import rest_framework as filters 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

 
from store.models import Brand,     CategoryPlaceTable, CategoryTable, Characteristic, CharacteristicType, ParentCharacteristic, Product  



from store.serializers import BrandSerializer,    CategoryPlaceTableSerializer,   CategoryTableSerializer, CharacteristicSerializer, CharacteristicTypeSerializer, ParentCharacteristicSerializer,  ProductSerializer

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

class CharacteristicTypeTypeViewSet(viewsets.ModelViewSet):
    queryset=CharacteristicType.objects.all()
    serializer_class=CharacteristicTypeSerializer

class ParentCharacteristicViewSet(viewsets.ModelViewSet):
    queryset=ParentCharacteristic.objects.all()
    serializer_class=ParentCharacteristicSerializer

class CharacteristicViewSet(viewsets.ModelViewSet):
    queryset=Characteristic.objects.all()
    serializer_class=CharacteristicSerializer

     

class CategoryTableViewSet(viewsets.ModelViewSet):
        queryset=CategoryTable.objects.all()
        serializer_class=CategoryTableSerializer
        # filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]   
        # filterset_fields=['name', 'level']
        # ordering_fields=['level','name', 'parent']
        # ordering=['level']
        filter_backends = (filters.DjangoFilterBackend,)
        filterset_fields = ('name','id')

class CategoryPlaceTableViewSet(viewsets.ModelViewSet):
        queryset=CategoryPlaceTable.objects.all()
        serializer_class=CategoryPlaceTableSerializer  
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = ['id', 'parentId','categoryId', 'level']
        search_fields = ['=level', 'parentId','id']
        ordering_fields = ['level', 'id']
        ordering = ['level',]