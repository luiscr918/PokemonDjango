from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pokemons.models import Type
from pokemons.serializers import PokemonSerializer
from pokemons.serializers import TypeSerializer


@api_view(["POST"])
def guardar_type(request):
    serializer = TypeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def listar_types(_request):
    types = Type.objects.all()
    serializer = TypeSerializer(types, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def obtener_type_id(_request, type_id):
    try:
        type = Type.objects.get(id=type_id)
    except Type.DoesNotExist:
        return Response(
            {"mensaje": "type no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = TypeSerializer(type)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def actualizar_type(request, type_id):
    try:
        type = Type.objects.get(id=type_id)
    except Type.DoesNotExist:
        return Response(
            {"mensaje": "type no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = TypeSerializer(type, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def eliminar_type(_request, type_id):
    try:
        type = Type.objects.get(id=type_id)
    except Type.DoesNotExist:
        return Response(
            {"mensaje": "type no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )
    type.delete()
    return Response({"mensaje": "type eliminado correctamente"})
