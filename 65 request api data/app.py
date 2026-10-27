import requests

baseUrl = "https://pokeapi.co/api/v2/"

def getPokemonInfo(name):
    url = f"{baseUrl}/pokemon/{name}"
    respons = requests.get(url)
    if respons.status_code == 200:
        pokemonData = respons.json()
        return pokemonData
    else:
        print('failed to retireven dtadsa')

pokemonName = "pikachu"
pokemonInfo = getPokemonInfo(pokemonName)

if pokemonInfo:
    print(f"{pokemonInfo["name"]}") 
    print(f"{pokemonInfo["id"]}") 
    print(f"{pokemonInfo["height"]}") 
    print(f"{pokemonInfo["weight"]}") 