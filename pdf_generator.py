import pdfkit
import uuid


def gerar_pdf(html):

    nome = f"artigo_{uuid.uuid4().hex}.pdf"

    pdfkit.from_string(html, nome)

    return nome