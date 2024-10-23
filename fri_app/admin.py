from django.contrib import admin

# Register your models here.
from .models import Item

# Register UserProfile model
admin.site.register(Item)
