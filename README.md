# Ex02 Django ORM Web Application
## Date: 13/09/2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from.models import cardb,cardb_admin
admin.site.register(cardb,cardb_admin)

```


## OUTPUT

![alt text](<Screenshot (1).png>)

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
