

import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
from IPython.display import display
from deep_translator import GoogleTranslator
os.system('cls')

#criando tradutor e criando a tabela
tradutor = GoogleTranslator(source="en", target="pt")

#Criando a "Opçao" e falando para ele nao abrir o navegador visualmente falando e criando o navegador
options = Options()
options.add_argument("--headless") 
navegador = webdriver.Chrome(options = options)

#criando o numero do pokemon para a pesquisa da API e do WebDescreption
numeroPokemon = 8 #input("Digite o numero seu arrombado")

#abrindo o poke db e pesquisando o numero
url = f"https://pokemondb.net/pokedex/{numeroPokemon}"
navegador.get(url)

# #pesquisando a bios do pokemon
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
paragraphs = soup.find_all("p")
descricaoPokemon = paragraphs[:4]

# #traduzindo para PT
intro_text_ingles = "\n\n".join(p.text.strip() for p in descricaoPokemon)
intro_text_pt = tradutor.translate(intro_text_ingles)

#colocando time se for preciso e encerrando a ação 
time.sleep(2)
navegador.quit()
# entrando na API
url = f"https://pokeapi.co/api/v2/pokemon/{numeroPokemon}"
response = requests.get(url)
dados = response.json()

if response.status_code == 200: #numeor correto é o 200
    tiposPokemon = ""
    listTipoPokemon = []
    habilidadesPokemon = ""
    listHabilidadesPokemons = []
    hpPokemon = ""
    attackPokemon = ""
    defensePokemon = ""
    specAtck = ""
    specDef = ""
    speed = ""


    # print(f"\n=== Dados do Pokémon #{numeroPokemon} ===")
    # print("Nome:", dados["name"])
    
    
    # print("\nTipos:")
    for tipo in dados["types"]:
        listTipoPokemon.append(tipo["type"]["name"])
        tiposPokemon = "-".join(listTipoPokemon)
        # print("-", tipo["type"]["name"])
        # print(textoTeste)
        # tiposPokemon = ("-", tipo["type"]["name"])

    

    # print("\nHabilidades:")
    for habilidade in dados["abilities"]:
        # print("-", habilidade["ability"]["name"])  
        listHabilidadesPokemons.append(habilidade["ability"]["name"])
        habilidadesPokemon = "-".join(listHabilidadesPokemons)
    
    # print("\nStats:")
    for stat in dados["stats"]:
        nome_stat = stat["stat"]["name"]
        match nome_stat: 
            case "hp":
                hpPokemon = stat["base_stat"]
            case "attack":
                attackPokemon = stat["base_stat"]
            case "defense":
                defensePokemon = stat["base_stat"]
            case "special-attack":
                specAtck = stat["base_stat"]
            case "special-defense":
                specDef = stat["base_stat"]
            case "speed":
                speed = stat["base_stat"]

        # valor = stat["base_stat"]
        # print(f"- {nome_stat}: {valor}")
    nomePokemon = dados["name"]    
    # print(f"aqui :{habilidadesPokemon}")
    
else:
    print(f"Erro ao acessar a API: {response.status_code}")

tabela = pd.read_excel("Pasta1.xlsx")

#Criando a nova linha teste
novaLinha = {
    'Pokemon': nomePokemon ,
    'Numero': numeroPokemon,
    'Tipo': tiposPokemon,
    'Habilidades': habilidadesPokemon,
    'Hp': hpPokemon,
    'Attack': attackPokemon,
    'Def': defensePokemon,
    'Bio':intro_text_pt
}

#adicionando a nova linha na tabela e mostrando ela no terminal
tabela = pd.concat([tabela, pd.DataFrame([novaLinha])], ignore_index=True)
display(tabela)
tabela.to_excel('pokemon_tabela.xlsx', index=False)