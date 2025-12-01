"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Importamos settings para manejar archivos media
from django.conf.urls.static import (
    static,
)  # Importamos static para manejar archivos media

# 1. Imports de DRF
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Login: Recibe user/pass, devuelve Access Token + Refresh Token
    TokenRefreshView,  # Refresco: Recibe Refresh Token, devuelve nuevo Access Token
)

# Importamos el ViewSet desde la app
from pedidos.views import ProductoViewSet, CategoriaViewSet, PedidoViewSet

# 2. Configuración del Router (Nivel Proyecto)
router = DefaultRouter()
router.register(r"productos", ProductoViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"pedidos", PedidoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Esto habilita /accounts/login/, /accounts/logout/, etc.
    path("accounts/", include("django.contrib.auth.urls")),
    # RUTA WEB (MVT) - Todo lo visual entra por /menu/
    # Delegamos todo lo que empiece con "menu/" a nuestra app de pedidos
    path("menu/", include("pedidos.urls")),
    # RUTA API (DRF) - Todo lo de la API entra por /api/
    path("api/", include(router.urls)),
    # Rutas para JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# Configuración para servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
