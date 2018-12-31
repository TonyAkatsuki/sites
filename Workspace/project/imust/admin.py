from django.contrib import admin

# Register your models here.
from .models import Student,StuArt,Article,Comment,News

admin.site.register(Student)
admin.site.register(StuArt)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(News)