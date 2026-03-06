from PyPDF2 import PdfReader


def extrair_texto_pdf(file):

    reader = PdfReader(file)

    texto = ""

    for page in reader.pages:
        texto += page.extract_text() + "\n"

    return texto