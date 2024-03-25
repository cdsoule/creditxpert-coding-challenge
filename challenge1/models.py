from django.db import models

class Shape(models.Model):
    name = models.CharField(max_length=200)
    fa_class = models.CharField(max_length=200)

class ColorScheme(models.Model):
    color1 = models.CharField(max_length=40)
    color2 = models.CharField(max_length=40)
    color3 = models.CharField(max_length=40)
    color4 = models.CharField(max_length=40)
