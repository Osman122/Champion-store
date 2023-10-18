from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
      return f"{self.name}"

class Product(models.Model):
    
    "name, age,  image, created , updated at"
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=10 ,null=False)
    image = models.ImageField(upload_to='champions/images' ,null=True ,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, null=True, blank=True,editable=False,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)

  


    def __str__(self):
      return f"{self.name}"
    
    
    def get_image_url(self):
       return f"/media/{self.image}"
    
    @classmethod
    def get_all(cls):
        return  cls.objects.all()