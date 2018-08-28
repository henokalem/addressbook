# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Address(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phoneNumber = models.PositiveIntegerField()
    emailAddress = models.EmailField()
    streetAddress = models.TextField()
    owner = models.CharField(max_length=30)

    def __str__(self):
        return self.firstName+' '+self.lastName