from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
import uuid


# Create your models here.
class Product(models.Model):

    # Product related stuff.
    id                      = models.CharField(max_length=100, primary_key=True)
    name                    = models.CharField(max_length=60)
    brand_name              = models.CharField(max_length=50)
    total_weight            = models.CharField(max_length=30)
    serving_size            = models.CharField(max_length=50)
    calories                = models.CharField(max_length=30)

    #Macros per serving
    fat                     = models.CharField(max_length=30)
    saturated_fat           = models.CharField(max_length=30)
    trans_fat               = models.CharField(max_length=30)
    cholesterol             = models.CharField(max_length=30)
    sodium                  = models.CharField(max_length=30)
    carbohydrate            = models.CharField(max_length=30)
    fibre                   = models.CharField(max_length=30)
    sugars                  = models.CharField(max_length=30)
    protein                 = models.CharField(max_length=30)

    # Micros per serving
    vitamin_a               = models.CharField(max_length=30)
    vitamin_c               = models.CharField(max_length=30)
    calcium                 = models.CharField(max_length=30)
    iron                    = models.CharField(max_length=30)

    ingredients             = models.TextField(blank=True)
    allergens               = models.TextField(blank=True)

    logos                   = models.CharField(max_length=60)
    ocr_text                = models.TextField(blank=True)
    image_front_url         = models.TextField(blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return '#{} - {} by {}'.format(self.id, self.name, self.brand_name)
