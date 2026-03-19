from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pokemons.models import Pokemon
from pokemons.serializers import PokemonSerializer
from pokemons.serializers import TypeSerializer


@api_view(["POST"])
def guardar_pokemon(request):
    serializer = PokemonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def listar_pokemons(_request):
    pokemons = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemons, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def obtener_pokemon_id(_request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return Response(
            {"mensaje": "pokemon no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = PokemonSerializer(pokemon)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def actualizar_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return Response(
            {"mensaje": "pokemon no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = PokemonSerializer(pokemon, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def eliminar_pokemon(_request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return Response(
            {"mensaje": "pokemon no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    pokemon.delete()
    return Response({"mensaje": "Pokemon eliminado correctamente"})
