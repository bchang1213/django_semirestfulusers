# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
	context = {
		'users': User.objects.all()
	}
	print context
	return render(request, "semirestful_users/index.html", context)

def new(request):
	return render(request, "semirestful_users/new.html")

def create(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags='dookie')
			return redirect('/new')
	else:
		user = User.objects.create()
		user.name = request.POST['name']
		user.email = request.POST['email']
		user.save()
		return redirect('/')

def show(request, user_id):
	context = {
		'users': User.objects.get(id= user_id)
	}
	return render(request, "semirestful_users/user.html", context)

def edit(request, user_id):
	context = {
		'user' : User.objects.get(id = user_id)
	}
	return render(request, "semirestful_users/edit.html", context)

def alter(request, user_id):
	userupdate = User.objects.get(id = user_id)
	userupdate.name = request.POST['name']
	userupdate.email = request.POST['email']
	userupdate.save()
	return redirect ('/')

def delete(request, user_id):
	deleteuser = User.objects.get(id = user_id)
	deleteuser.delete()
	return redirect('/')