from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class posts(models.Model):
    Title=models.CharField(max_length=30)
    Content=models.TextField()
    Image=models.ImageField(default='default.jpg',upload_to='blog_pics')
    Posted=models.TimeField(auto_now_add=True)
    Author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")

    def __str__(self):
        return f'{self.Title}'

    def get_absolute_url(self):
        #return reverse('Individual',kwargs={'pk':self.pk})
        return reverse('home')
            
