# Desafio Cacau RPA

Este repositório contém scripts de automação em Python e uma API simples para realizar o processo de download de arquivos, extração de dados de planilhas e preenchimento de formulários web. O objetivo é automatizar tarefas simples de manipulação de dados e interação com formulários.

---

## Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Clonando o repositório](#clonando-o-repositório)
3. [Configurando o ambiente virtual](#configurando-o-ambiente-virtual)
4. [Instalando as dependências](#instalando-as-dependências)
5. [Executando a API](#executando-a-api)
6. [Executando o Script de Automação](#executando-o-script-de-automação)

---

## Pré-requisitos

Antes de começar, verifique se você possui os seguintes pré-requisitos instalados:

### Python 3

Você pode verificar se o Python está instalado executando o seguinte comando:

```bash
python --version
Ou, dependendo do sistema:

bash
Copiar código
python3 --version
Caso não tenha o Python instalado, faça o download da versão mais recente na página oficial do Python.

Clonando o repositório
Para começar, clone este repositório em sua máquina local utilizando o Git. No terminal, execute o seguinte comando:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Configurando o ambiente virtual
É recomendável usar um ambiente virtual para isolar as dependências do projeto.

No Windows
Abra o prompt de comando ou PowerShell.

Navegue até o diretório do projeto:

bash
Copiar código
cd caminho/dir/meu-dir
Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
Ative o ambiente virtual:

bash
Copiar código
.\venv\Scripts\activate
No Linux/macOS
Abra o terminal.

Navegue até o diretório do projeto:

bash
Copiar código
cd caminho/dir/meu-dir
Crie um ambiente virtual:

bash
Copiar código
python3 -m venv venv
Ative o ambiente virtual:

bash
Copiar código
source venv/bin/activate
Instalando as dependências
Após ativar o ambiente virtual, instale as dependências do projeto utilizando o arquivo requirements.txt. Execute o seguinte comando no terminal:

bash
Copiar código
pip install -r requirements.txt
Isso irá instalar todas as bibliotecas necessárias para o funcionamento do projeto.

Executando a API
Agora, você está pronto para executar a API. Para isso, execute o seguinte comando no terminal:

Navegue até o diretório da API:

bash
Copiar código
cd caminho/dir/meu-dir
Execute o arquivo app.py:

Caso esteja usando o Python 2:

bash
Copiar código
python app.py
Ou, caso esteja usando o Python 3 explicitamente:

bash
Copiar código
python3 app.py
A API será iniciada e estará disponível no endereço especificado (geralmente http://localhost:3000). Mude para a porta da sua preferência, se necessário.

Executando o Script de Automação
Abra uma nova aba de terminal no mesmo diretório onde está o seu repositório.

Ative o ambiente virtual na nova aba, caso ainda não tenha feito:

No Windows:
bash
Copiar código
.\venv\Scripts\activate
No Linux/macOS:
bash
Copiar código
source venv/bin/activate
Execute o script de automação que consome a API. No terminal, execute o seguinte comando:

Caso esteja usando o Python 2:

bash
Copiar código
python automation_script.py
Ou, caso esteja usando o Python 3 explicitamente:

bash
Copiar código
python3 automation_script.py
Isso executará o script de automação que irá consumir a API, realizar o download dos arquivos, processá-los e preencher o formulário conforme os dados extraídos.
