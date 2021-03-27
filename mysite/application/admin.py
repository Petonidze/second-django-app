# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import user, notes

admin.site.register(user)
admin.site.register(notes)
# Register your models here.
