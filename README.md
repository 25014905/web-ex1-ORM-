# Ex01 Django ORM Web Application
## Date: 

## AIM
To develop a Django Application to store and retrieve data from an Online Food Delivery Database platform like Zomato or Swiggy using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
MODELS.PY
```
from django.db import models
from django.contrib import admin

class FoodApp(models.Model):
    OrderID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Date = models.DateField()
    ItemName = models.CharField(max_length=100)
    Amount = models.FloatField()
    

class FoodAppAdmin(admin.ModelAdmin):
    list_display = (
        'OrderID',
        'Name',
        'Date',
        'ItemName',
        'Amount',
    )

```

ADMIN.PY
```
from django.contrib import admin
from .models import FoodApp, FoodAppAdmin

admin.site.register(FoodApp, FoodAppAdmin)
```


## OUTPUT


<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/0a8244f7-2740-4b7f-8f22-6a617e135c69" />

DEVELOPED BY: MIRDULA D
REGISTRATION NO. 212225040234

## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
