from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    choices_title = models.JSONField(default=list)
    cover = models.ImageField(upload_to="obrazky/")
    def __str__(self):
        return self.title  
    
    
