import requests
from config import AZURE_KEY, AZURE_REGION, AZURE_ENDPOINT


def traduzir_texto(texto, idioma_destino):

    path = f"/translate?api-version=3.0&to={idioma_destino}"

    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_KEY,
        "Ocp-Apim-Subscription-Region": AZURE_REGION,
        "Content-Type": "application/json"
    }

    body = [{"text": texto[:5000]}]

    response = requests.post(
        AZURE_ENDPOINT + path,
        headers=headers,
        json=body
    )

    resultado = response.json()

    return resultado[0]["translations"][0]["text"]


def traduzir_elementos(elementos, idioma_destino, progress_callback=None):

    total = len(elementos)
    contador = 0

    for el in elementos:

        if el["tipo"] == "texto":

            el["conteudo"] = traduzir_texto(
                el["conteudo"],
                idioma_destino
            )

        contador += 1

        if progress_callback:
            progress_callback(contador / total)

    return elementos