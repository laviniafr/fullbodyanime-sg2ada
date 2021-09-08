from django.db import models

class Sample(models.Model):
  title = models.CharField(max_length=100)
  image = models.FilePathField(path="/img")
  description = models.CharField(max_length=100)

class Prototype(models.Model):
  title = models.CharField(max_length=100)
  image = models.FilePathField(path="/img")
  description = models.CharField(max_length=100)
 