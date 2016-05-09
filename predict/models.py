from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Urllist(models.Model):
	url = models.URLField(max_length=200)
	title = models.CharField(max_length=20,default="title")


