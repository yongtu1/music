from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('<int:board_num>/', views.search),
    path('<int:board_pk>/like/',views.like, name='like'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),
    path('<int:board_pk>/<int:comment_pk>/comment_delete/', views.comment_delete, name='comment_delete'),
    path('<int:board_pk>/comments_create/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    path('<int:board_pk>/detail/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
]
