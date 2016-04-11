from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Category,Plan,Company,PhoneCompany,Item,Link,LinksCompany,Image,DetPlan
from django.db.models import Q




def new_add(request):
	return render(request,'index.html')


class Adlist(ListView):
	model=Company
	paginate_by=12
	context_object_name ='companies'



class AdDetail(DetailView):
	model=Company
	context_object_name ='company'

def search(request):
	query = request.GET.get('query','')
	if query:
		qset=(
			Q(name__icontains=query) |
			Q(aboutUs__icontains=query) |
			Q(category__name__icontains=query)|
			Q(tags__title__icontains=query)
		)
		companies= Company.objects.filter(qset).distinct()
	else:
		companies=Company.objects.all()
	
	template = loader.get_template('ads/company_list.html')
	context ={

		'query':query,
		'companies':companies

	}
	return HttpResponse(template.render(context,request))