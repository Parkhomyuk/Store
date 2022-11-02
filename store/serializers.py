 
 

from asyncio.windows_events import NULL
from xml.dom import ValidationErr
from rest_framework import serializers

from store.models import Brand,  CategoryPlaceTable, CategoryTable, Characteristic, CharacteristicType, FeedBack, FeedBackCascade, FeedBackOpinion, FeedBackOpinionType, FeedBackVote, ParentCharacteristic, ParentCharacteristicType, PriceProduct, PriceProductRepresent, Product

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Brand
class PriceProductSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model=PriceProduct    
        fields='__all__'
    
     
    def validate(self,obj):
        if obj['date_end'] < obj['date_start']:
            raise serializers.ValidationError('End date should be greater than Start Date')
        return obj    

class PriceProductRepresentSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model=PriceProductRepresent    
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    #brand=serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
    # created_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # updated_by = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    price=serializers.SerializerMethodField()   
    status=serializers.SerializerMethodField()
    feedbacks_count=serializers.SerializerMethodField()
    class Meta: 
        # fields=('name', 'description', 'feedbacks', 'feedbacks_count', 'images', 'price', 'rating', 'status', 'subcategory',   'brand','created_at', 'updated_at')
        fields='__all__'
        model=Product
        # extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault()}, 'update_by': {'default': serializers.CurrentUserDefault()}} 
     
    def get_price(self, obj):
        price_c=PriceProductRepresent.objects.filter(product=obj.id) 
         
          
        if len(price_c)>0:                   
            return PriceProductRepresentSerializer(price_c, many=True).data[0]['price']
        else:                
             

            return 0    
    def get_status(self, obj):
        price_c=PriceProductRepresent.objects.filter(product=obj.id)         
          
        if len(price_c)>0:                   
            return 1
        else:      
            return 0
    # def get_feedbacks_count(self, obj):
    #     fidbacks=
     
 

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

class PriceProductSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model=PriceProduct    
        fields='__all__'
    
     
    def validate(self,obj):
        if obj['date_end'] < obj['date_start']:
            raise serializers.ValidationError('End date should be greater than Start Date')
        return obj    

class PriceProductRepresentSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model=PriceProductRepresent    
        fields='__all__'

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBack
        fields='__all__'        

class FeedBackOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBackOpinion  
        fields='__all__'      

    def validate(self, obj):
        print('object', obj)
        if obj['opinion']>5 or obj['opinion']<1 :
            raise serializers.ValidationError('Opinion should be more than 0 and less or equal 5')
        return obj    

class FeedBackVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBackVote  
        fields='__all__'

    def validate(self,obj):
        if obj['positive_vote']==True and obj['negative_vote']==True  :
            raise serializers.ValidationError('Only one type of vote should be added')
          

        else :
            return obj     
           

class FeedBackCascadeSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBackCascade 
        fields='__all__'

class FeedBackOpinionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBackOpinionType 
        fields='__all__'

