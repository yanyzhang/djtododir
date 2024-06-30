from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('add', views.addItem, name='add'),
    path('completed/<todo_id>', views.completedTask, name='completed'),
    path('delete_completed/', views.deleteCompleted, name='delete_completed'),
    path('delete_all/', views.deleteAll, name='delete_all'),
    path('show_delete_all_modal/', views.showDeleteAllModal, name='show_delete_all_modal'),

]

