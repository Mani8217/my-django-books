from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    rating = models.CharField(max_length=20, default='Unknown')
    image_url = models.URLField(max_length=500, null=True, blank=True)  
    

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books'