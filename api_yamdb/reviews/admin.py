from django.contrib import admin
from .models import Title, Category, Genre, User


admin.site.register(User)
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)