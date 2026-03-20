import requests
from django.core.management.base import BaseCommand
from pokemons.models import Pokemon, Type


class Command(BaseCommand):
    help = "Importa los primeros 500 Pokémon desde la PokéAPI"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Iniciando importación..."))

        url = "https://pokeapi.co/api/v2/pokemon?limit=500"
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Error al conectar con la PokéAPI"))
            return

        data = response.json()

        for item in data["results"]:
            # Obtener detalle de cada pokemon
            detail_response = requests.get(item["url"])
            p = detail_response.json()

            # 1. Crear o obtener el Pokémon (evita duplicados)
            pokemon, created = Pokemon.objects.get_or_create(
                pokedex_id=p["id"],
                defaults={
                    "name": p["name"].capitalize(),
                    "image_url": p["sprites"]["other"]["official-artwork"][
                        "front_default"
                    ],
                    "hp": p["stats"][0]["base_stat"],
                    "attack": p["stats"][1]["base_stat"],
                    "defense": p["stats"][2]["base_stat"],
                    "speed": p["stats"][5]["base_stat"],
                    "height": p["height"] / 10,  # La API los da en decímetros
                    "weight": p["weight"] / 10,  # La API los da en hectogramos
                },
            )

            # 2. Manejar los Tipos (Many-to-Many)
            for t in p["types"]:
                tipo_nombre = t["type"]["name"].capitalize()
                tipo_obj, _ = Type.objects.get_or_create(name=tipo_nombre)
                pokemon.types.add(tipo_obj)

            if created:
                self.stdout.write(f"Sincronizado: {pokemon.name}")
            else:
                self.stdout.write(f"Saltado (ya existe): {pokemon.name}")

        self.stdout.write(self.style.SUCCESS("¡Importación completada con éxito!"))
