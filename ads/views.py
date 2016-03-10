from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Category,Plan,Company,PhoneCompany,Item,Link,LinksCompany,Image,Map,DetPlan


# Create your views here.
class CategoryList(ListView):
	model=Category

class CategoryDetail(DetailView):
	model=Category
class PlanList(ListView):
	model=Plan

