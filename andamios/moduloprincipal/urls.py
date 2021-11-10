from django.urls import path, include
from .views import home, eliminarandamio, agregarandamio, listarandamios, usuariocreacion, cliente, ClienteViewset, modificarandamio, AlquilerViewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'alquiler', AlquilerViewset)
router.register(r'cliente', ClienteViewset)

#localhost:8000/api/producto

urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
    path('usuario/', usuariocreacion, name="usuario"),
    path('agregar-andamio/', agregarandamio, name="agregarandamio"),
    path('listar-andamio/', listarandamios, name="listarestablecimientos"),
    path('modificar-andamio/<id>/', modificarandamio, name="modificarandamio"),
    path('eliminar-andamio/<id>/', eliminarandamio, name="eliminarandamio"),
    #path('usuariocontacto/', usuariocontacto, name="usuario-contacto"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]