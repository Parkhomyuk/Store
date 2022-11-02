 
from email.policy import default
from itertools import product
from django.db import models
from django.contrib.auth.models import User

from accounts.models import CustomUser
 
 

 

class CategoryTable(models.Model):
    name=models.CharField(max_length=255, unique=True)
    final_level=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class CategoryPlaceTable(models.Model):
    categoryId=models.ForeignKey(CategoryTable, on_delete=models.CASCADE, related_name='category')
    parentId=models.ForeignKey(CategoryTable, on_delete=models.CASCADE, related_name='parent')
   
    level=models.IntegerField()
    class Meta:
        ordering = ('level',)
    def __str__(self):      
        return  f"{self.parentId} /{self.categoryId}"

class Brand(models.Model):
    name=models.CharField(max_length=255, unique=True)
    description=models.TextField()
    def __str__(self):
        return self.name 
    


class Product(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField()
    feedbacks= models.IntegerField(default=0)
    feedbacks_count=models.IntegerField()
    images= models.IntegerField(default=0)
    price= models.FloatField(default=0.0)
    rating= models.FloatField(default=0.0)
    status= models.IntegerField(default=1)
    subcategory=models.ForeignKey(CategoryTable, on_delete=models.CASCADE)
    created_by=models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='contributed_by')
    updated_by=models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='updated_by')
    brand=models.ForeignKey(Brand, on_delete=models.RESTRICT,  null=False, blank=False )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ParentCharacteristicType(models.Model):
    name=models.CharField(max_length=255)   
    def __str__(self):
        return self.name      

class ParentCharacteristic(models.Model):
    name=models.ForeignKey(ParentCharacteristicType, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    

class CharacteristicType(models.Model):
    name=models.CharField(max_length=255)
    parent=models.ForeignKey(ParentCharacteristicType, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Characteristic(models.Model):
    name=models.ForeignKey(CharacteristicType, on_delete=models.CASCADE)
    value=models.CharField(max_length=255)
    parentCharacteristic=models.ForeignKey(ParentCharacteristicType,  on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.value
     
class PriceProduct(models.Model):     
    create_by=models.ForeignKey(CustomUser, on_delete=models.RESTRICT, related_name='admin_create')
    update_by=models.ForeignKey(CustomUser, on_delete=models.RESTRICT,related_name='admin_update')
    date_create= models.DateTimeField(auto_now_add=True)
    date_update= models.DateTimeField(auto_now=True)
    date_start= models.DateTimeField()
    date_end= models.DateTimeField(null=True)
    def __str__ (self):
        return 'from '+f'{self.date_start}'.split(' ',1)[0]+' to '+f'{self.date_end}'.split(' ',1)[0]
    

class PriceProductRepresent(models.Model):
    product=models.ForeignKey(Product, on_delete=models.RESTRICT)
    price_list=models.ForeignKey(PriceProduct, on_delete=models.RESTRICT)
    price=models.FloatField()
    def __str__(self):
        return f'{self.product}-{self.price}'


class FeedBack(models.Model):
    product=models.ForeignKey(Product,related_name='feedback_product', on_delete=models.RESTRICT, null=False, blank=False)   
    user=models.ForeignKey(CustomUser, on_delete=models.RESTRICT, null=False, blank=False)
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    term_of_use=models.CharField(max_length=255)
    advantages=models.TextField(null=True, blank=True)
    limitations=models.TextField(null=True, blank=True)
    comments=models.TextField(null=True, blank=True)
    additionals=models.TextField(null=True, blank=True)
    photos=models.TextField(null=True, blank=True)
    # def __str__(self):
    #     return self.product

class FeedBackVote(models.Model):
    feedback=models.ForeignKey(FeedBack, related_name='feedback_voted', on_delete=models.RESTRICT)
    positive_vote=models.BooleanField(default=False)
    negative_vote=models.BooleanField(default=False)

class FeedBackCascade(models.Model):
    parent_feedback=models.ForeignKey(FeedBack, related_name='feedback_parent', on_delete=models.RESTRICT, null=False, blank=False)
    child_feedback=models.ForeignKey(FeedBack, related_name='feedback_child', on_delete=models.RESTRICT, null=False, blank=False)
    current_feedback=models.ForeignKey(FeedBack, related_name='feedback_current', on_delete=models.RESTRICT)
    def __str__(self):
        return self.current_feedback

class FeedBackOpinionType(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class FeedBackOpinion(models.Model):
    feedback=models.ForeignKey(FeedBack, related_name='feedbacks_opinion', on_delete=models.RESTRICT)
    appearance=models.ForeignKey(FeedBackOpinionType, related_name='feedbacks_opinion', on_delete=models.CASCADE)
    opinion=models.IntegerField()
    

