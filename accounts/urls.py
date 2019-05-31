from django.urls import path, include
from . import views

app_name= 'accounts'

urlpatterns = [
    path('change_passowrd/',views.change_passowrd, name='change_passowrd'),
    path('edit/',views.edit, name='edit'),
    path('delete/',views.delete, name='delete'),
    path('logout/',views.logout, name='logout'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
]