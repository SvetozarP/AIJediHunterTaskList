from django.urls import path
from . import views

from django.http import HttpResponseNotFound


def ignore_well_known(request, *args, **kwargs):
    return HttpResponseNotFound()


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),                       # manual form
    path('add-random/', views.add_random_task, name='add_random_task'),  # ← new
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('.well-known/<path:path>', ignore_well_known),
]