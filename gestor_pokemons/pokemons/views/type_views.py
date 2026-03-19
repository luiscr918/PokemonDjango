from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pokemons.models import Type
from pokemons.serializers import PokemonSerializer
from pokemons.serializers import TypeSerializer