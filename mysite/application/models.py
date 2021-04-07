# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django import forms

class application_user(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    birth_date = models.DateField()
    status = models.CharField(max_length = 140) # determine by admin thanks user`s activity
    biography = models.TextField()

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.biography

class notes(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length = 255)
    text = models.TextField()
    author = models.ForeignKey(application_user, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.title


    