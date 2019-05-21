from django.db import models

class Save(models.Model):
    saving = models.TextField()
    

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    writer = models.TextField()
    
    def __str__(self):
        return self.title

