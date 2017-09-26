# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect

def index(request):
	users = User.objects.all()
	print users
	return render(request, "semirestful_users/index.html")

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
