from rest_framework import serializers
from .models import Pokemon
from .models import Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["id", "name"]


class PokemonSerializer(serializers.ModelSerializer):
    types = serializers.PrimaryKeyRelatedField(many=True, queryset=Type.objects.all())
    def to_representation(self, instance):
        """
            Muestra el objeto completo al hacer GET, pero acepta IDs al hacer POST/PUT.
        """
        representation = super().to_representation(instance)
        representation['types'] = TypeSerializer(instance.types.all(), many=True).data
        return representation
    class Meta:
        model = Pokemon
        fields = [
            "id",
            "pokedex_id",
            "name",
            "image_url",
            "hp",
            "attack",
            "defense",
            "speed",
            "height",
            "weight",
            "types"
        ]
