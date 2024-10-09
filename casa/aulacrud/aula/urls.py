from django.urls import path
from . import views

app_name = 'aula'
urlpatterns = [
    path('pessoa/', views.pessoa_lista, name='pessoa_lista'),
    path('casa/', views.casa_lista, name='casa_lista'),
]