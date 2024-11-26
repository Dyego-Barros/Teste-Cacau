# Guia para Criar e Ativar um Ambiente Virtual Python

Este guia ensina como criar e ativar um ambiente virtual Python em sistemas operacionais Linux, macOS e Windows. Além disso, também mostra como instalar as dependências a partir de um arquivo `requirements.txt`.

## Passo 1: Instalando o Python e o `virtualenv`

Antes de criar um ambiente virtual, você precisa ter o Python e o `virtualenv` instalados no seu sistema.

### 1.1 Linux/MacOS
No Linux e no macOS, o Python já vem pré-instalado na maioria das distribuições. Para verificar se você tem o Python instalado, use o comando:

```bash
python3 --version

#Crie o Ambiente virtual
python3 -m venv venv

#Ativando o ambiente
source venv/bin/activate

#Instalando os requirements
pip install -r requirements.txt
```

###1.2 Windows
No Windows, faça o download do Python na página oficial [https://www.python.org/downloads/]. Para verificar se você tem o Python instalado, use o comando:

```bash
python --version

#Crie o Ambiente virtual
python -m venv venv

#Ativando o ambiente
.\venv\Scripts\activate

#Instalando os requirements
pip install -r requirements.txt
```

### 2 Instruções para execução
Após a ativação do Virtualenvironment e instalção dos pcotes, precisamos abrir duas  abas de terminal, uma para executar o projeto web de exemplo e outra para executar a automação

```bash
#Navegue até o diretorio webserver_test
cd /webserver_tes

#Execute o projeto
python3 app.py  #Ele executará um servidor web na portal 3000, você pode trocar pela porta de sua preferência.
```

```bash
#Navegue até o diretorio raiz do projeto e execute o arquivo Automation.py
python3 Automation.py #Ele executará  o script de automação proposto no teste
 
