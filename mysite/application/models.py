# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class user(models.Model):
    birth_date = models.DateField()
    status = models.CharField(max_length = 140)
    biography = models.TextField()
    def __str__(self):
        return self.biography

class notes(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length = 255)
    text = models.TextField()
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.title