from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail

def new_Contact(request):
	
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save();
			contact.save()
			fullname=request.POST.get('fullname')
			email=request.POST.get('email')
			message=request.POST.get('message')
			send_mail('Envio de Formulario de Contacto',message,'directoriopopayan@gmail.com',['directoriopopayan@gmail.com'],fail_silently=False)
			return HttpResponseRedirect('/')
	else:
		form = ContactForm()
		
	template= loader.get_template('index.html')

	context = {
		'form':form
	}
	return HttpResponse(template.render(context, request))

def home(request):
	form = ContactForm()
	return render(request,'index.html',{'form':form})
