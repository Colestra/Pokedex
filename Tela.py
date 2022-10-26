import PySimpleGUI as sg
import json
import requests
from ApiPokemon import buscar_pokemon
from ApiPokemon import buscar_id_evolucao
from PIL import Image
import urllib.request
from io import BytesIO

layout = [
    [sg.Text("Nome Pokemon")],
    [sg.InputText(key="pokemon")],
    [sg.Button("Buscar Pokemon")],
    [sg.Text("", key="texto_pokemon")],
    [sg.Text("", key="habilidade")],
    [sg.Image(key="imagemPokemon")],

    [sg.Text("", key="evolucao1")],
    [sg.Image(key="imagemevolucao1")],

    [sg.Text("", key="evolucao2")],
    [sg.Image(key="imagemevolucao2")],

]

janela = sg.Window("Pokedex", layout)

while True:
    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED:
        break
    if evento == "Buscar Pokemon":
        codigo_pokemon = valores["pokemon"]

        pokemon, habilidades, imagem = buscar_pokemon(codigo_pokemon)
        pokemon, nome_evolucao1, nome_evolucao2, imagem_evolucao1, imagem_evolucao2 = buscar_id_evolucao(codigo_pokemon)

        janela["texto_pokemon"].update(f"Pokemon : {codigo_pokemon}")
        janela["habilidade"].update(f"Habilidades : {habilidades}")
        janela["evolucao1"].update(f"Evolução 1 : {nome_evolucao1}")
        janela["evolucao2"].update(f"Evolução 2 : {nome_evolucao2}")
        print(imagem_evolucao1)

        urllib.request.urlretrieve(imagem,"pokemon.png")
        janela["imagemPokemon"].update("pokemon.png")

        urllib.request.urlretrieve(imagem_evolucao1, "evolucao1pokemon.png")
        janela["imagemevolucao1"].update("evolucao1pokemon.png")

        img3 = urllib.request.urlretrieve(imagem_evolucao2, "evolucao2pokemon.png")
        janela["imagemevolucao2"].update("evolucao2pokemon.png")

janela.close()