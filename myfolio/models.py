from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import CharField, EmailField

# Create your models here.

class PersonalData(models.Model):
    profile_image = models.ImageField(upload_to = 'pics')
    post = models.CharField(max_length=100)
    about = models.TextField()
    current_city = models.CharField(max_length=100)
    full_address = models.TextField()
    age = models.IntegerField() 
    email = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=100)

class CodingSkills(models.Model):
    skill_name = models.CharField(max_length=100)
    in_progress = models.IntegerField()

class DevelopmentSkills(models.Model):
    skill_name = models.CharField(max_length=100)
    in_progress = models.CharField(max_length=100)

class Education(models.Model):
    year_of_completion = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    about_course = models.TextField()
class Experience(models.Model):
    year_of_completion = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    about_course = models.TextField()

class Counter(models.Model):
    hackerank_star = models.CharField(max_length=100)
    project_complete = models.CharField(max_length=100)
    project_ongoing = models.CharField(max_length=100)
    internship =  models.CharField(max_length=100)

class mywork(models.Model):
    img = models.ImageField(upload_to = "pics")
    title = models.CharField(max_length=100)
    catogary = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)

class Tags(models.Model):
    tag_name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
 
class Querry(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subect = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    date  = models.DateTimeField(auto_now=True)

class Subscibe(models.Model):
    email = CharField(max_length=100)

class Document(models.Model):
    resume = models.FileField(upload_to='document')

class links(models.Model):
    facebook = CharField(max_length=1000)
    instgram = CharField(max_length=1000)
    github = CharField(max_length=1000)
    linkedin = CharField(max_length=1000)
    resume = CharField(max_length=1000)
