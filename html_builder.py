def construir_html(elementos):

    html = "<html><body style='font-family:Arial;'>"

    for el in elementos:

        if el["tipo"] == "texto":

            html += f"<{el['tag']}>{el['conteudo']}</{el['tag']}>"

        elif el["tipo"] == "imagem":

            html += f"<img src='{el['src']}' style='max-width:100%;'><br><br>"

        elif el["tipo"] == "codigo":

            html += f"<pre style='background:#eee;padding:10px;'>{el['conteudo']}</pre>"

    html += "</body></html>"

    return html