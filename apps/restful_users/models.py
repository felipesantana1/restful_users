# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UsersManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'Names must contain more than 1 Character'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Names must contain more than 1 Character'
        if len(postData['email']) < 11:
            errors['email'] = 'Email must contain more than 11 Character'
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UsersManager()
