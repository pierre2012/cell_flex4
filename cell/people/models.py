from django.db import models
from django.contrib.admin import widgets
from django import forms
from datetime import date

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class Person(models.Model):
    TYPE = (
            (0 , 'Faculty'),
            (1 , 'Post Doc'),
            (2 , 'Grad student'),
            (3 , 'Undergrad'),
            (4 , 'Collaborator'),
            (5 , 'Alumni'),
    )

    name = models.CharField(max_length=250, blank=True)

    member_type = models.IntegerField(choices=TYPE, default=4, null=True)

    title = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    short_bio = models.TextField(blank=True)
    publications_name = models.TextField(blank=True)
    website = models.CharField(blank=True,max_length=250)

    image = models.ImageField(upload_to='people/', blank=True)
    sortorder = models.IntegerField(blank=True, null=True)
    
    
    
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

    class Admin:
        pass

    def __unicode__(self):
        return self.name
 