from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('Moto', MotoViewSet)
router.register('Saisie', SaisieViewSet)
router.register('Papiers', PapiersViewSet)
router.register('Commissariat', CommissariatViewSet)
router.register('Agent_Police', Agent_PoliceViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
 
]