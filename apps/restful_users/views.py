# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import Users

def users(request):
    context = {

        'users' : Users.objects.all()

    }
    return render(request, 'restful_users/users.html', context)

def add(request):
    return render(request, 'restful_users/add.html')

def edit(request, id):
    context = {

        'user' : Users.objects.get(id=id)

        }

    return render(request, 'restful_users/edit.html', context)

def display(request, id):
    context = {

        'user' : Users.objects.get(id=id)

    }
    return render(request, 'restful_users/show.html', context)

def create(request):
    context = {

        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email']

    }
    Users.objects.create(first_name = context['first_name'], last_name = context['last_name'], email = context['email'])

    return redirect('/users')

def changes(request, id):

    edit = Users.objects.get(id=id)
    edit.first_name = request.POST['first_name']
    edit.last_name = request.POST['last_name']
    edit.email = request.POST['email']
    edit.save()

    return redirect('/users')

def delete(request, id):
    x = Users.objects.get(id=id)
    x.delete()
    return redirect('/users')

def back(request):
    return redirect('/users')
