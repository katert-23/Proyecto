from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    
    path('index', views.index,name='index'),
    path('home',views.Home,name="home"),
    path('servicios',views.servicios, name="Servicios"),
    path('ropa',views.ropa, name="ropa"),
    path('registrate',views.registrate, name="Registrate"),
    path('base',views.base, name="base"),
    path('crear', views.crear,name='crear'),
    path('editar<int:id>', views.editar,name='editar'),
    path('foto', views.foto,name='foto'),
    path('index', views.index,name='index'),
    path('eliminar<int:id>', views.eliminar,name='eliminar'),
   # path('descarga', views.descarga,name='descarga'),
    
   
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

