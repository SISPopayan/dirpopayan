from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.home, name='home'),
	url(r'^contact/$',views.new_Contact, name='contact'),
	url(r'^categoria/(?P<slug>[-\w]+)/$',views.category_show,name='category_show'),
	
]