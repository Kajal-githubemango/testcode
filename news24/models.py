from django.utils import timezone
from django.db import models

class contact(models.Model):
   name= models.CharField(max_length=100, null=True, blank=True) 
   email= models.EmailField(null=True, blank=True) 
   subject= models.CharField(max_length=100, null=True, blank=True) 
   meassage= models.TextField(null=True, blank=True) 
   
   def __str__(self):
      return self.name

category = [
				('Tech', 'Tech'), 
				('Sports', 'Sports'), 
				('Fashion', 'Fashion'), 
            ('Business', 'Business'), 
            ('Entertainment', 'Entertainment'),
            ('Latest_News', 'Latest_News'), 
				]
class news(models.Model):
   category = models.CharField(max_length=100, choices=category,    null=True, blank=True)
   title= models.CharField(max_length=100, null=True, blank=True) 
   details= models.TextField(null=True, blank=True) 
   time= models.DateTimeField(default = timezone.now, null=True, blank=True) 
   image= models.ImageField(upload_to ='images/') 
   
   def __str__(self):
      return self.category
   