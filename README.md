# 📝 Tradutor de Artigos com IA / AI Article Translator

[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/AlexTDO/tradutor-artigos-ia)](https://github.com/AlexTDO/tradutor-artigos-ia/stargazers)

---

## 🔹 Descrição / Description

**Português:**
Ferramenta de tradução de artigos científicos utilizando Inteligência Artificial. Permite ler PDFs, HTML e TXT, extrair conteúdo, traduzir e gerar arquivos traduzidos automaticamente. Ideal para pesquisadores, estudantes e profissionais.

**English:**
AI-powered article translation tool. Reads PDFs, HTML, and TXT, extracts content, translates, and generates translated files automatically. Perfect for researchers, students, and professionals.

---

## 🔹 Demonstração / Demo

![Demo do Tradutor](https://media.giphy.com/media/26xBuwEsl9b3gHh6E/giphy.gif)
*GIF ilustrativo mostrando a tradução de um artigo*
*Illustrative GIF showing article translation*

---

## 🔹 Funcionalidades / Features

* Leitura de documentos PDF, HTML e TXT / Read PDF, HTML, and TXT files
* Tradução automática via IA / AI-powered translation
* Geração de arquivos traduzidos / Generate translated files
* Modular, extensível e fácil de configurar / Modular, extensible, and easy to configure

---

## 🔹 Pré-requisitos / Requirements

* Python 3.10 ou superior / Python 3.10 or higher
* Instalar dependências / Install dependencies:

```bash
pip install -r requirements.txt
```

* API de IA configurada (Azure ou OpenAI) / Configured AI API (Azure or OpenAI)

---

## 🔹 Instalação / Installation

```bash
# Clonar o repositório / Clone the repository
git clone https://github.com/AlexTDO/tradutor-artigos-ia.git
cd tradutor-artigos-ia

# Instalar dependências / Install dependencies
pip install -r requirements.txt
```

---

## 🔹 Uso / Usage

```bash
# Executar o tradutor / Run the translator
python main.py

# Gerar PDF traduzido / Generate translated PDF
python pdf_generator.py
```

> Ajuste credenciais em `config.py` se necessário / Adjust credentials in `config.py` if needed.

---

## 🔹 Estrutura do Projeto / Project Structure

```text
tradutor-artigos-ia/
│
├── app.py              # Script principal / Main script
├── main.py             # Entrada do tradutor / Translator entry
├── pdf_generator.py    # Geração de PDFs traduzidos / Generate translated PDFs
├── pdf_reader.py       # Leitura de PDFs / PDF reader
├── translator.py       # Módulo de tradução / Translation module
├── scraper.py          # Captura de conteúdo / Content scraper
├── html_builder.py     # Construção de arquivos HTML / HTML builder
├── requirements.txt    # Dependências / Dependencies
└── .gitignore          # Arquivos ignorados pelo Git / Git ignore
```

---

## 🔹 Contribuição / Contributing

1. Fork este repositório / Fork this repository
2. Crie uma branch para sua feature / Create a feature branch
3. Faça commit das alterações / Commit your changes
4. Envie um Pull Request / Open a Pull Request

---

## 🔹 Licença / License

Este projeto está licenciado sob a [MIT License](LICENSE) / This project is licensed under the MIT License.
