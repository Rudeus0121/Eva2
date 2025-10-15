# salud_vital/urls.py
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    # --- Admin (solo referencia, no se usa) ---
    path('admin/', admin.site.urls),

    # --- API REST (Django REST Framework) ---
    # 👇 Esta es la correcta, debe apuntar a clinica/urls
    path('api/', include('clinica.urls')),

    # --- Documentación interactiva ---
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # --- Templates HTML (interfaz web + home) ---
    path('', include('clinica.urls_templates')),
]
