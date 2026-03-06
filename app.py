import streamlit as st
from scraper import extrair_estrutura
from translator import traduzir_elementos, traduzir_texto
from html_builder import construir_html
from pdf_generator import gerar_pdf
from pdf_reader import extrair_texto_pdf


st.title("AI Article Translator")

modo = st.radio(
    "Escolha como deseja traduzir",
    ["Traduzir Link", "Upload de PDF"]
)

idiomas = {
    "Português": "pt",
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Chinês": "zh-Hans",
    "Japonês": "ja",
    "Coreano": "ko",
    "Italiano": "it",
    "Russo": "ru"
}

idioma = st.selectbox("Idioma da tradução", list(idiomas.keys()))

# -----------------------------
# TRADUÇÃO DE LINK
# -----------------------------

if modo == "Traduzir Link":

    url = st.text_input("Cole o link do artigo")

    if st.button("Traduzir artigo"):

        st.write("Extraindo estrutura do artigo...")

        elementos = extrair_estrutura(url)

        progress = st.progress(0)

        def atualizar(p):
            progress.progress(p)

        elementos = traduzir_elementos(
            elementos,
            idiomas[idioma],
            atualizar
        )

        html = construir_html(elementos)

        st.success("Tradução concluída")

        st.components.v1.html(html, height=600, scrolling=True)

        if st.button("Gerar PDF"):

            with st.spinner("Gerando PDF..."):

                pdf_path = gerar_pdf(html)

            with open(pdf_path, "rb") as f:

                st.download_button(
                    "Baixar PDF",
                    f,
                    file_name="artigo_traduzido.pdf"
                )

            st.success("PDF gerado com sucesso")

            st.experimental_rerun()


# -----------------------------
# TRADUÇÃO DE PDF
# -----------------------------

elif modo == "Upload de PDF":

    uploaded_file = st.file_uploader(
        "Envie um arquivo PDF",
        type="pdf"
    )

    if uploaded_file:

        st.write("Extraindo texto do PDF...")

        texto = extrair_texto_pdf(uploaded_file)

        progress = st.progress(0)

        def atualizar(p):
            progress.progress(p)

        st.write("Traduzindo PDF...")

        traducao = traduzir_texto(
            texto,
            idiomas[idioma]
        )

        html = f"<html><body>{traducao}</body></html>"

        st.success("Tradução concluída")

        st.write(traducao)

        if st.button("Gerar PDF Traduzido"):

            with st.spinner("Gerando PDF..."):

                pdf_path = gerar_pdf(html)

            with open(pdf_path, "rb") as f:

                st.download_button(
                    "Baixar PDF",
                    f,
                    file_name="pdf_traduzido.pdf"
                )

            st.success("PDF gerado com sucesso")

            st.experimental_rerun()