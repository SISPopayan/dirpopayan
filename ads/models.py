from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class Category(models.Model):
	name=models.CharField(max_length=140)
	description=models.CharField(max_length=255)
	image=models.ImageField(blank=True)
	slug=AutoSlugField(populate_from='name')

	def __str__(self):
		return self.name

	def get_companies(self):
		return self.company_set.all()



type_ads=(
	('BASICO','Basico'),
	('FINDME','FindMe'),
	('STARTUP','StartUp'),
)

class Plan(models.Model):
	title=models.CharField(max_length=255)
	description=models.TextField()
	mounthPrice=models.DecimalField(max_digits=12,decimal_places=2)
	yearPrice=models.DecimalField(max_digits=12,decimal_places=2)
	numberImage=models.PositiveSmallIntegerField()
	numberPhone=models.PositiveSmallIntegerField()
	type_ad=models.CharField(choices=type_ads,default='BASICO',max_length=10)

	def __str__(self):
		return self.title

class Company(models.Model):
	name=models.CharField(max_length=255)
	phone_number = models.CharField(max_length=30)
	address=models.CharField(max_length=255)
	email=models.EmailField()
	logo=models.ImageField()
	aboutUs=models.TextField()
	plan=models.ForeignKey(Plan)
	ranking=models.PositiveIntegerField(default=0)
	slug = AutoSlugField(populate_from='name')
	links=models.ManyToManyField('Link',through='LinksCompany')
	category=models.ForeignKey(Category)
	lat=models.FloatField()
	lng=models.FloatField()
	tags=models.ManyToManyField('Tag',through='CompanyTags')

	def __str__(self):
		return self.name
	def  get_images(self):
		return self.image_set.all()
	def get_phones(self):
		return self.phonecompany_set.all()
	def get_links(self):
		return self.linkscompany_set.all()
	def get_items(self):
		return self.item_set.all()
	
class Tag(models.Model):
	title=models.CharField(max_length=255)

class CompanyTags(models.Model):
	company=models.ForeignKey(Company)
	tag=models.ForeignKey(Tag)



class PhoneCompany(models.Model):
	company=models.ForeignKey(Company)
	phone=models.CharField(max_length=30)
	description=models.CharField(max_length=255)

	def __str__(self):
		return self.phone

class Item(models.Model):
	company=models.ForeignKey(Company)
	title=models.CharField(max_length=255)
	description=models.TextField()
	price=models.PositiveIntegerField(default=0)
	image=models.ImageField(blank=True)

	def __str__(self):
		return self.title

class Link(models.Model):
	title=models.CharField(max_length=255)
	icon=models.ImageField()

	def __str__(self):
		return self.title

class LinksCompany(models.Model):
	company=models.ForeignKey(Company)
	link=models.ForeignKey(Link)
	url=models.CharField(max_length=255)


class Image(models.Model):
	title=models.CharField(max_length=255)
	alt=models.CharField(max_length=255)
	image=models.ImageField()
	company=models.ForeignKey(Company)


class DetPlan(models.Model):
	plan=models.ForeignKey(Plan)
	company=models.ForeignKey(Company)
	startDate=models.DateField()
	finishDate=models.DateField()
	seller=models.ForeignKey(User)


