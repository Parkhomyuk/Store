from dataclasses import field, fields
 
from pyexpat import model
from rest_framework import serializers

from store.models import Brand,  CategoryPlaceTable, CategoryTable, Characteristic, CharacteristicType, ParentCharacteristic, ParentCharacteristicType, Product

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

 

class ParentCharacteristicTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=ParentCharacteristicType

class CharacteristicTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model= CharacteristicType        

class ParentCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        field='__all__'
        model= ParentCharacteristic

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        field='__all__'
        model= Characteristic        

       

 
class CategoryPlaceTableSerializer(serializers.ModelSerializer):
    child=serializers.SerializerMethodField()
    def get_child(self, obj):
        children=CategoryPlaceTable.objects.filter(parentId=obj.categoryId)
        return CategoryPlaceTableSerializer(children, many=True).data 
    class Meta:
        fields=['id','parentId','level','categoryId','child' ]
        model=CategoryPlaceTable           

        

class CategoryTableSerializer(serializers.ModelSerializer):
    # child=serializers.StringRelatedField(many=True)    
    # child=serializers.PrimaryKeyRelatedField(many=True, read_only='True')    
    level=serializers.SerializerMethodField()   
    parent=serializers.SerializerMethodField()
    def get_level(self, place):
        level_n = CategoryPlaceTable.objects.filter(categoryId=place.id).order_by('-level')
        if len(CategoryPlaceTableSerializer(level_n, many=True).data)>0:
            return CategoryPlaceTableSerializer(level_n, many=True).data[0]['level']
        else:
            return None    
    def get_parent(self,category):
        children=CategoryPlaceTable.objects.filter(categoryId=category.id)  
        if len(CategoryPlaceTableSerializer(children, many=True).data)>0:
            res=CategoryTableSerializer(CategoryTable.objects.filter(id=CategoryPlaceTableSerializer(children, many=True).data[0]['parentId']), many=True).data[0]['name']
             
            return res
        else:
            return None       
     
    class Meta:
        # fields=['id','name','level','parent']
        fields='__all__'
        model=CategoryTable    
        ordering=('level',)  