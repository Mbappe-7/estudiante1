from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluimos todas las rutas de la app estudiantes
    path('', include('estudiantes.urls')),
]
