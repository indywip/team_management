from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.team_form, name='team_insert'), 
    path('<int:id>/', views.team_form, name='team_update'), 
    path('delete/<int:id>/', views.team_delete, name='team_delete'),
    path('list/', views.team_list, name='team_list'),
]
