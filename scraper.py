import requests
from bs4 import BeautifulSoup


def extrair_estrutura(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    elementos = []

    for tag in soup.find_all(["h1","h2","h3","p","img","pre","code"]):

        if tag.name in ["h1","h2","h3","p"]:

            texto = tag.get_text().strip()

            if texto:
                elementos.append({
                    "tipo": "texto",
                    "tag": tag.name,
                    "conteudo": texto
                })

        elif tag.name == "img":

            src = tag.get("src")

            if src:
                elementos.append({
                    "tipo": "imagem",
                    "src": src
                })

        elif tag.name in ["pre","code"]:

            codigo = tag.get_text()

            elementos.append({
                "tipo": "codigo",
                "conteudo": codigo
            })

    return elementos