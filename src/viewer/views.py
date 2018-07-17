from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.http import JsonResponse
from .models import Code


def show(request, room):  # TODO: render room info
    return render(request, "viewer/showroom.html", {'room': room})


def edit(request, room):
    if request.user.is_authenticated:  # TODO: Plus this room belongs to him or not to edit
        return render(request, "viewer/editable.html", {'room': room})
    else:
        return redirect(reverse('login'))


def save(request):
    # TODO: save ROOM CODE and Check Whether it's coming from Author
    if request.user.is_authenticated and request.method == 'POST':
        try:
            code = request.POST['code']
        except KeyError:
            return JsonResponse({'error': 'no code?'})
        # TODO: change to edit Code object
        Code(source=code, author=request.user).save()
        return JsonResponse({'status': 'success'})


def do_login(request):
    if request.method == 'GET':
        return render(request, 'viewer/login.html')
    elif request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/edit/spider')
            else:
                return render(request, 'viewer/login.html', {'message': 'Wrong Password & Login'})
        except KeyError:
            return redirect(reverse('showroom'))


def do_logout(request):
    logout(request)
    return redirect(reverse('login'))
