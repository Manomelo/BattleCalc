import requests
import json
import os

def pokemonName(name: str):
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(name)
    response = requests.get(url, timeout=2)
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        stats = json.dumps(data["stats"], indent=4)
        # print("{}'s Id: {}".format(data["name"], data["id"]))
        # print("{}'s Name: {}".format(data["name"],data["name"]))
        # print("{}'s Height: {}".format(data["name"], data["height"]))
        # print("{}'s Weight: {}".format(data["name"],data["weight"]))
        # print("{}'s Stats: {}".format(data["name"],data["stats"][1]['stat']['name']))
        print(stats)

pokemonName("mewtwo")
pokemonName("mew")
pokemonName("clefable")