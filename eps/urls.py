"""
URL configuration for eps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api.views import*
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('Vehicule', VehiculeViewSet)
router.register('Piece', PieceViewSet)
router.register('Engin', EnginViewSet)
router.register('Saisie', SaisieViewSet)
router.register('Papiers', PapiersViewSet)
router.register('Commissariat', CommissariatViewSet)

# schema_view = get_schema_view(
#  openapi.Info(
#      title="API Documentation",
#      default_version='v1',
#      contact=openapi.Contact(email="contact@example.com"),
#  ),
#  public=True,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include(router.urls)),
    path('backend/', include('backend.urls')),
    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
