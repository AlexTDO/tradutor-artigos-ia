import streamlit as st
from scraper import extrair_texto
from translator import traduzir_texto

st.title("Tradutor de Artigos com Azure AI")

st.write("Cole o link de um artigo em inglês para traduzir automaticamente para português.")

url = st.text_input("Link do artigo")

if st.button("Traduzir artigo"):

    if url:

        st.write("Extraindo texto do artigo...")

        texto = extrair_texto(url)

        st.write("Traduzindo artigo...")

        traducao = traduzir_texto(texto)

        st.success("Tradução concluída")

        st.subheader("Artigo traduzido")

        st.write(traducao)

        st.download_button(
            "Baixar artigo traduzido",
            traducao,
            file_name="artigo_traduzido.txt"
        )

    else:

        st.warning("Por favor insira um link válido.")