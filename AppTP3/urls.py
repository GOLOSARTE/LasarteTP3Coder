from django.urls import path
from .views import inicio, alumnos, profesores, curso, buscar_curso
from AppTP3 import views

urlpatterns = [

    path('', inicio, name='inicio'),
    path('alumnos/', alumnos, name='alumnos'),
    path('profesores/', profesores, name='profesores'),
    path('curso/', curso, name='curso'),
    path('buscar-curso/', buscar_curso, name="buscar_curso")
]
 
