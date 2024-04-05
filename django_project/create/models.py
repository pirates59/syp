from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("create-post-detail", kwargs={"pk": self.pk})
    
        



class Profile(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
    
