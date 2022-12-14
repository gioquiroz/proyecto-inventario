from pyexpat import model
from tkinter import CASCADE
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class TablaPeliculas(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self) :
        return self.title


class TablaNueva(models.Model):
    cedula = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    def __str__(self) :
        return self.name, self.cedula



