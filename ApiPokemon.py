import json
import requests

global pokemon, pokemonUrl, pokemonUrlFim
#pokemon = input("Pokemon: ")
#print(pokemon)





def buscar_pokemon(pokemon):
    #print("Pokemon:" ,pokemon)
    pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/').json()
    habilidades = []
    for i in pokemon['abilities']:
        habilidades.append(i['ability']['name'])
        #habilidades = habilidades.append(i['ability']['name'])
        print(habilidades)
        print("Habilidade :", i['ability']['name'])
    imagem = pokemon['sprites']['front_default']
    print("Imagem Pokemon :", pokemon['sprites']['front_default'])
    return pokemon, habilidades, imagem


def buscar_id_evolucao(pokemon):
    pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{pokemon}/').json()
    pokemonUrl = pokemon['evolution_chain']['url']
    #print("Url da Evolução:", pokemonUrl)
    res = requests.get(pokemonUrl).json()
    #print(res.headers)
    for i in res['chain']['evolves_to']:
        nome_evolucao1 = i['species']['name']
        print("Evolução 1 :", nome_evolucao1)
        imagem_evolucao1 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome_evolucao1}/').json()
        imagem_evolucao1 =  imagem_evolucao1['sprites']['front_default']
        for e in res['chain']['evolves_to'][0]['evolves_to']:
            nome_evolucao2 = e['species']['name']
            print("Evolução 2 :", nome_evolucao2)
            imagem_evolucao2 = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nome_evolucao2}/').json()
            imagem_evolucao2 = imagem_evolucao2['sprites']['front_default']
    return pokemon, nome_evolucao1, nome_evolucao2, imagem_evolucao1, imagem_evolucao2

    #print("Evolução Pokemon : ", res['chain']['evolves_to'][0]['evolves_to'][0]['species']['name'])

#buscar_pokemon(pokemon)
#buscar_id_evolucao(pokemon)


