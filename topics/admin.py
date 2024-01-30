from django.contrib import admin
from .models import Topic, Category, Comment
# Register your models here.

admin.site.register(Topic)
admin.site.register(Category)
admin.site.register(Comment)