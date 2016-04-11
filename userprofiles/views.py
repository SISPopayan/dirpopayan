from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.


def authentication(request):
	if request.method =='POST':
		action = request.POST.get('action',None)
		username = request.POST.get('email',None)
		password = request.POST.get('password',None)

		if action == 'signup':
			user = User.objects.create_user(username=username, password=password)
			user.save()
		elif action == 'login':

			user= authenticate(username=username , password= password)
			if user is not None:
				login(request, user)
				return redirect('/')
			return redirect('/login')

		return redirect('/')

	return render(request,'login.html',{})	
