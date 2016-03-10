from __future__ import unicode_literals

from django.db import models



class Contact(models.Model):
	fullname=models.CharField(max_length=255)
	email=models.EmailField()
	phone=models.CharField(max_length=30)
	message=models.TextField()


	def __str__(self):
		return self.fullname
