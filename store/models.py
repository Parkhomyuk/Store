 
from email.policy import default
from enum import unique
from django.db import models
 
 

 

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
    name=models.CharField(max_length=255)
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
    
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
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
     
