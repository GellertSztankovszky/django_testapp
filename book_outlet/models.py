from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(null=True, max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_bestselling = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])
    

    def __str__(self):  
        return f"{self.title} ({self.author}) score: {self.rating}"
