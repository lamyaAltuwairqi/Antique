from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class Category(models.Model):
    name=models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=300)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images')
    details=models.TextField()
    email=models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])
    
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


