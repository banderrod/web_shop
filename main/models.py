from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name