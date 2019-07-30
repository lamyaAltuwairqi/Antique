from django.contrib import admin
from .models import Category, Items, Profile

# Register your models here.

admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Profile)

