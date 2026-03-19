from django.urls import path, include

urlpatterns = [
    path("pokemons/", include("pokemons.urls.pokemon_urls")),
    path("types/", include("pokemons.urls.type_urls")),
]
