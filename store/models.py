from django.db import models

class Brand(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name 
class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name        
class Subcategory(models.Model):
    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category,related_name='subcategories'  , on_delete=models.CASCADE)
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
    subcategory=models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    characteristic=models.IntegerField(default=0) 
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
   


