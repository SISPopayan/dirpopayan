from django.conf.urls import url
from .import views

urlpatterns=[
	
	url(r'^empresas/$',views.Adlist.as_view(), name='list'),
	url(r'^(?P<slug>[-\w]+)$',views.AdDetail.as_view(),name='detail'),
	url(r'^tubusqueda/$', views.search, name='search'),

]