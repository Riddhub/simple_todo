from django.urls import path

from todo.views import *

urlpatterns = [
    path("", index, name='index'),
    path("completeTodo/id:<todo_id>", completeTodo, name='completeTodo'),
    path("deleteComplete", deleteComplete, name='deleteComplete'),
    path("deleteAll", deleteAll, name='deleteAll'),
]
