from django.urls import path
from pokemons.views import type_views

urlpatterns = [
    path("crear/", type_views.guardar_type),
    path("listar/", type_views.listar_types),
    path("obtener/<int:type_id>/", type_views.obtener_type_id),
    path("actualizar/<int:type_id>/", type_views.actualizar_type),
    path("eliminar/<int:type_id>/", type_views.eliminar_type),
]