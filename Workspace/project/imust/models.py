from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=18, primary_key=True)
    password = models.CharField(max_length=8)
    name = models.CharField(max_length=40)

class StuArt(models.Model):
    sid = models.CharField(max_length=18)
    aid = models.IntegerField()

class Article(models.Model):
    aid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    cid = models.IntegerField(primary_key=True)
    aid = models.IntegerField()
    sid = models.CharField(max_length=18)
    name = models.CharField(max_length=40)
    comment = models.TextField()
    time = models.DateTimeField(auto_now=True)

class News(models.Model):
    nid = models.IntegerField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    time = models.TextField()
