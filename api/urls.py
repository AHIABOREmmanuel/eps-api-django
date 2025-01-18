from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('Vehicule', VehiculeViewSet)
router.register('Piece', PieceViewSet)
router.register('Engin', EnginViewSet)
router.register('Saisie', SaisieViewSet)
router.register('Papiers', PapiersViewSet)
router.register('Commissariat', CommissariatViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
]