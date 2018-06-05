from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns=[
	url(r'^index/$',views.index, name='index'),
	url(r'^login/$',views.login,name='login'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^register/$',views.register,name='register'),
]