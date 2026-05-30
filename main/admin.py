from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Post, Product, News

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(News)