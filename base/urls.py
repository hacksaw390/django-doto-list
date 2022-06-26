from django.contrib import admin
from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpate, TaskDelete, LoginUser, RegisterUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register', RegisterUser.as_view(), name='register'),

    path('login-user', LoginUser.as_view(), name='login-user'),
    path('logout-user', LogoutView.as_view(next_page='login-user'), name='logout-user'),


    path('', TaskList.as_view(), name='tasks'),
    path('task-detail/<int:pk>', TaskDetail.as_view(), name='task-detail'),
    path('task-update/<int:pk>', TaskUpate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
]
