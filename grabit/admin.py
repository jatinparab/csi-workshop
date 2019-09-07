from django.contrib import admin
from .models import Item

# Register your models here.


@admin.register(Item)
class Item(admin.ModelAdmin):
    fields = ('title', 'description', 'img', 'is_worthy')
    list_display = ('title', 'description', 'is_worthy')