from django.urls import path
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import register_todolist
from todolist.views import login_todolist
from todolist.views import logout_todolist
from todolist.views import update_todolist
from todolist.views import delete_todolist

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register_todolist, name='register_todolist'),
    path('login/', login_todolist, name='login_todolist'),
    path('logout/', logout_todolist, name='logout_todolist'),
    path('update/<int:id>/', update_todolist, name='update_todolist'),
    path('delete/<int:id>/', delete_todolist, name='delete_todolist'),
]