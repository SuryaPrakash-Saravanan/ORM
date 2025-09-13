from django.db import models
from django.contrib import admin

class cardb(models.Model):
    car_name = models.CharField(max_length=30)
    regno=models.IntegerField(primary_key=True)
    car_owner_email=models.EmailField()
    date=models.DateField()
    mileage=models.FloatField()
    colour = models.CharField()
    
class cardb_admin(admin.ModelAdmin):
    list_display=["car_name","regno","car_owner_email","date","mileage","colour"]