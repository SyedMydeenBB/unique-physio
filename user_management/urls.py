from django.urls import path,include
from .views import *

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('user_registration/', user_registration, name='user_registration'),
    path('user_list/', user_list, name='user_list'),
    path('user_edit/<pk>/', user_edit, name='user_edit'),
    path('user_view/<pk>/', user_view, name='user_view'),
    path('user_delete/<pk>/', user_delete, name='user_delete'),
    path('roles/', roles, name='roles'),
    path('roles_create/', roles_create, name='roles_create'),
    path('roles_edit/<pk>/', roles_edit, name='roles_edit'),
    path('roles_delete/<pk>/', roles_delete, name='roles_delete'),
    path('permission/<pk>/', permission, name='permission'),
    path('function_setup/', function_setup, name='function_setup'),
    
]