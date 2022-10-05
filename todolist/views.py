from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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
# TODO : IMPLEMENTASI BUTTON MARK AS FINIHED/UNFINISHED


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
def update_todolist(request, id):
    task = Task.objects.get(user=request.user, pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
def delete_todolist(request, id):
    task = Task.objects.get(user=request.user, pk=id)
    print(id)
    task.delete()
    return redirect("todolist:show_todolist")