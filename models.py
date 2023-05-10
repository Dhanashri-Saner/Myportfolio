from django.db import models

# Create your models here.

class CareerDetails(models.Model):
    photo = models.ImageField(upload_to='image/')
    birth = models.CharField(max_length=100)
    age = models.IntegerField()
    website = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    freelance= models.CharField(max_length=100)
    class Meta:
        db_table = 'CareerDetails'

class Skills(models.Model):
    skillname  = models.CharField(max_length=100)
    skillpercent = models.IntegerField()

class Testimonial(models.Model):
    tmname = models.CharField(max_length=100)
    tmexpertise = models.CharField(max_length=100)
    tmdesc = models.TextField(max_length=300)
    tmimg = models.ImageField()
    


