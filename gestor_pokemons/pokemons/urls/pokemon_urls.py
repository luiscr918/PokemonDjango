from django.urls import path
from pokemons.views import pokemon_views

urlpatterns = [
    path("crear/", pokemon_views.guardar_pokemon),
    path("listar/", pokemon_views.listar_pokemons),
    path("obtener/<int:pokemon_id>/", pokemon_views.obtener_pokemon_id),
    path("actualizar/<int:pokemon_id>/", pokemon_views.actualizar_pokemon),
    path("eliminar/<int:pokemon_id>/", pokemon_views.eliminar_pokemon),
]
