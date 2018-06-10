from __future__ import unicode_literals
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

from .models import *

def index(request):
	return render(request, 'index.html')

def regist(request):
	if not request.user.is_authenticated(): 
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			repassword = request.POST.get('repassword')
			if password == repassword:
				check_user = User.objects.filter(username=username)
				if len(check_user) == 0:
					user = User.objects.create_user(username, '', password)
					user.backend = 'django.contrib.auth.backends.ModelBackend'
					auth.login(request, user)
					return redirect('/magicsite/menu/')
				else: return HttpResponse("<script>alert('使用者名稱重複');window.location = '/magicsite/register/';</script>")
			else: return HttpResponse("<script>alert('密碼與確認密碼不同');window.location = '/magicsite/register/';</script>")
		return render(request,'register.html')
	else: return redirect('/magicsite/menu/')

def login(request):
	if not request.user.is_authenticated(): 
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/magicsite/menu/')
		else: return render(request, 'login.html')
	else: return redirect('/magicsite/menu/')

def logout(request):
	auth.logout(request)
	return redirect('/login/')

@login_required
def menu(request):
	question_sets = Question_Set.objects.all()
	return render(request, 'menu.html', {'question_sets': question_sets})

@login_required
def question(request):
		print(int(request.POST.get('option')))
		question_sets_id=int(request.POST.get('option'))
		question_sets = Question_Set.objects.get(id=question_sets_id)
		question = Question.objects.filter(question_set__id=question_sets_id)	
		return render(request, "question.html", {'question': question})

@login_required
def wand(request):
	max = int(request.POST.get('max'))
	request.session['key'] = max
	if max > 0:
		if max == 1:
			magic_wand = Magic_Wand.objects.get(name='吸塵器')
		elif max == 2:
			magic_wand = Magic_Wand.objects.get(name='吹泡泡')
		elif max == 3:
			magic_wand = Magic_Wand.objects.get(name='拍立得')
		elif max == 4:
			magic_wand = Magic_Wand.objects.get(name='MP3')
		return render(request, 'wand.html',{'magic_wand':magic_wand})		
	return render(request, "wand.html")


@login_required
def result(request):
	max = request.session['key'] 
	if max > 0:
		if max == 1:
			magic_wand = Magic_Wand.objects.get(name='吸塵器')
			mahou_Shoujo = magic_wand.mahou_shoujo
		elif max == 2:
			magic_wand = Magic_Wand.objects.get(name='吹泡泡')
			mahou_Shoujo = magic_wand.mahou_shoujo
		elif max == 3:
			magic_wand = Magic_Wand.objects.get(name='拍立得')
			mahou_Shoujo = magic_wand.mahou_shoujo
		elif max == 4:
			magic_wand = Magic_Wand.objects.get(name='MP3')
			mahou_Shoujo = magic_wand.mahou_shoujo
		return render(request, 'result.html',{'magic_wand':magic_wand,'mahou_Shoujo':mahou_Shoujo})		
	return render(request, "result.html")
	