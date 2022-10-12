from django.urls import reverse
from django.contrib import messages
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.username
    data = Task.objects.filter(user=request.user)
    context = {
        'todolist': data,
        'username': username,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def todolist_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(user=user, title=title, description=description)
        response = redirect("todolist:show_todolist")
        return response

    context = {}
    return render(request, "create_task.html", context)

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(user=user, title=title, description=description)
    return HttpResponse("Success")

def register_todolist(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created!")
            return redirect("todolist:login_todolist")
    
    context = {"form":form}
    return render(request, "register.html", context)

def login_todolist(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
        else:
            messages.info(request, "Wrong Username or Password!")
    
    context = {}
    return render(request, "login.html", context)

def logout_todolist(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_todolist'))
    return response

@login_required(login_url='/todolist/login/')
@csrf_exempt
def update_todolist(request, id):
    task = Task.objects.get(user=request.user, pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return HttpResponse("Success")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_todolist(request, id):
    task = Task.objects.get(user=request.user, pk=id)
    task.delete()
    return HttpResponse("Success")