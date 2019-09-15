from django.contrib import admin
from .models import User

# Register your models here.





# PRE DEFINED ###########################
@admin.register(User)
class User(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'is_worthy')
    list_display = ('first_name', 'last_name', 'email', 'is_worthy')