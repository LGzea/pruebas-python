import requests
from tabulate import tabulate

def obtener_pokemon(num_pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{num_pokemon}'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        pokemon = respuesta.json()
        return {
            'Número': pokemon['id'],
            'Nombre': pokemon['name'].capitalize(),
            'Tipo': ', '.join([tipo['type']['name'] for tipo in pokemon['types']])
        }
    else:
        return None

# Obtener información de los primeros 150 Pokémon
pokemon_data = [obtener_pokemon(i) for i in range(1, 10)]

# Filtrar posibles Pokémon nulos (si hubo algún error al obtener la información)
pokemon_data = [pokemon for pokemon in pokemon_data if pokemon is not None]

# Crear tabla
tabla = tabulate(pokemon_data, headers='keys', tablefmt='fancy_grid')

# Imprimir tabla
print(tabla)
