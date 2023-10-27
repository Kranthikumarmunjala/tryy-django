import pint
from django.conf import settings
from django.db import models

from.utils import number_str_to_float
from .validators import validate_unit_of_measure
"""
-Global
    -Ingredients
    -Recipes
-User
    -Ingredients
    -Recipes
        -Ingredients
        -Directions for Ingredients
"""

class Recipe(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name= models.CharField(max_length=220)
    description=models.TextField(blank=True,null=True)
    directions=models.TextField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

class RecipeIngredient(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    name=models.CharField(max_length=220)
    description=models.TextField(blank=True, null=True)
    quantity=models.CharField(max_length=50)   #1 1/4
    quantity_as_float=models.FloatField(blank=True, null=True)
    # pounds, lbs,oz,gram,etc
    unit=models.CharField(max_length=50, validators=[validate_unit_of_measure])  #pounds, lbs,oz,gram,etc
    direction=models.TextField(blank=True, null=True)
    timestamp =models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def convert_to_system(self, system="mks"):
        ureg=pint.UnitRegistry(system=system)
        measurement=self.quantity_as_float * ureg[self.unit]
        print(measurement)

    def as_mks(self):
        #meter, kilogram,second
        pass
    def as_imperial(self):
        #miles, pounds, seconds
        pass


    def save(self, *args, **kwargs):
        qty=self.quantity
        qty_as_float, qty_as_float_success=number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float=qty_as_float
        else:
            self.quantity_as_float=None
        super().save(*args, **kwargs)


