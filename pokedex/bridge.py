import pathlib

import requests

from PySide6.QtCore import QObject, Slot

from pokedex.settings import TEMP_FOLDER, ASSETS_FOLDER


class SearchPokemonBridge(QObject):
    @Slot(str, result=list)
    def fetch_pokemon(self, pokemon_query: str):
        image_path = TEMP_FOLDER / "pikachu.png"

        try:
            if image_path.exists():
                print("Deletando imagem")
                image_path.unlink()

            response = requests.get(
                f"https://pokeapi.co/api/v2/pokemon/{pokemon_query}"
            ).json()

            image_url = response["sprites"]["other"]["home"]["front_default"]
            image_content = requests.get(image_url).content

            filename = TEMP_FOLDER / f'{response["name"]}.png'
            with open(filename, "wb") as file:
                file.write(image_content)

            image_path = pathlib.Path(".") / ".." / "temp" / f'{response["name"]}.png'
            return str(image_path), response["name"].capitalize()
        except Exception as e:
            print(e)

            return str(pathlib.Path(".") / ".." / ASSETS_FOLDER / "not_found.png"), "Pokemon não encontrado!"
