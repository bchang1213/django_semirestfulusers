from __future__ import unicode_literals

from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) == 0:
            errors["name"] = "Please enter a name."
        if len(postData['email']) == 0:
            errors["email"] = "Please enter an e-mail."
        elif not EMAIL_REGEX.match(postData['email']):
        	errors["emailv"] = "Please enter a valid e-mail."
        return errors


class User(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
	def __repr__(self):
		return ("<User object:{} {} {}>".format(self.id, self.name, self.email))