import pathlib
import pint
import uuid

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
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


class RecipeQuerySet(models.QuerySet):
    def search(self,query=None):
        if query is None or query == "":
            return self.none()  #[]
        lookups = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(directions__icontains=query)
        )
        return self.filter(lookups)

class RecipeManager(models.Manager):
    def get_queryset(self):
        return RecipeQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)
'''
class Article(models.Model):
    user=models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=120)
    slug=models.SlugField(unique=True,blank=True, null=True)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateField(auto_now_add=False,auto_now=False, null=True,blank=True)

    objects=ArticleManager()

    def get_absolute_url(self):
        #return f'/artcles/{self.slug}/'
        return reverse("articles:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        #obj=Article.objects.get(id=1)
        #set somthing
        # if self.slug is None:
        #     self.slug=slugify(self.title)
        # if self.slug is None:
        #     slugify_instance_title(self, save=False)
        super().save(*args, **kwargs)
        #obj.save()
        #do another somthing


def article_pre_save(sender,instance,*args, **kwargs):
    #print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender,instance,created,*args, **kwargs):
    #print('post_save')
    if created:
        slugify_instance_title(instance,save=True)

post_save.connect(article_post_save, sender=Article)
'''
class Recipe(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name= models.CharField(max_length=220)
    description=models.TextField(blank=True,null=True)
    directions=models.TextField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    objects=RecipeManager()

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipess:detail", kwargs={"id": self.id})

    def get_hx_url(self):
        return reverse("recipess:hx-detail", kwargs={"id": self.id})


    def get_edit_url(self):
        return reverse("recipess:update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("recipes:delete", kwargs={"id":self.id})

    def get_ingrediets_chidren(self):
        return self.recipeingredient_set.filter()

def recipe_ingredient_image_upload_handler(instance, filename):
    fpath=pathlib.Path(filename)
    new_fname=str(uuid.uuid())  #uuid->uudid+timestamp
    return f"recipes/ingredient/{new_fname}{fpath.suffix}"

class RecipeIngredientImage(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=recipe_ingredient_image_upload_handler) #path/to/the/actual/file.png
    extracted=models.JSONField(blank=True, null=True)
    #image
    #extracted_text


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

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def get_delete_url(self):
        kwargs = {
            "parent_id": self.recipe.id,
            "id": self.id
        }
        return reverse("recipes:ingredient-delete", kwargs=kwargs)

    def get_hx_edit_url(self):
        kwargs={
            "parent_id":self.recipe.id,
            "id":self.id
        }
        return reverse("recipes:hx-ingredient-detail", kwargs=kwargs)


    def convert_to_system(self, system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg=pint.UnitRegistry(system=system)
        measurement=self.quantity_as_float * ureg[self.unit]
        return measurement #.to_base_units()

    def as_mks(self):
        #meter, kilogram,second
        measurement=self.convert_to_system(system='mks')
        return measurement.to_base_units()

    def as_imperial(self):
        #miles, pounds, seconds
        measurement = self.convert_to_system(system='imperial')
        return measurement.to_base_units()

    def save(self, *args, **kwargs):
        qty=self.quantity
        qty_as_float, qty_as_float_success=number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float=qty_as_float
        else:
            self.quantity_as_float=None
        super().save(*args, **kwargs)


