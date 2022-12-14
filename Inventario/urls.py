from django.urls import path
from Inventario import views
from .views import prueba,index,storage,movies,clients,registration, prueba
 
urlpatterns = [
    path('', index),
    path('storage/', storage),
    path('movies/',movies),
    path('clients/', clients),
    path('registration/', registration),
    path('prueba/', prueba)

]