Desafio Cacau RPA
Este repositório contém scripts de automação em Python e uma API simples para realizar o processo de download de arquivos, extração de dados de planilhas e preenchimento de formulários web. 
O objetivo é automatizar tarefas simples de manipulação de dados e interação com formulários.

Índice
1-Pré-requisitos
2-Clonando o repositório
3-Configurando o ambiente virtual
4-Instalando as dependências
5-Executando a API
6-Executando o Script de Automação
7-Pré-requisitos

Antes de começar, verifique se você possui os seguintes pré-requisitos instalados:

Python 3: Você pode verificar se o Python está instalado executando o seguinte comando:

python --version
Ou, dependendo do sistema:


python3 --version
Caso não tenha o Python instalado, faça o download da versão masi recente na pagina oficial do python



Clonando o repositório
Para começar, clone este repositório em sua máquina local utilizando o Git. No terminal, execute o seguinte comando:


git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/Dyego-Barros/Teste-Cacau.git)


Configurando o ambiente virtual
É recomendável usar um ambiente virtual para isolar as dependências do projeto.

No Windows:
Abra o prompt de comando ou PowerShell.

Navegue até o diretório do projeto:
cd caminho/dir/meu-dir

Crie um ambiente virtual:
python -m venv venv

Ative o ambiente virtual:
.\venv\Scripts\activate

No Linux/macOS:

Abra o terminal.
Navegue até o diretório do projeto:
cd caminho/dir/meu-dir

Crie um ambiente virtual:
python3 -m venv venv

Ative o ambiente virtual:
source venv/bin/activate

Instalando as dependências
Após ativar o ambiente virtual, instale as dependências do projeto utilizando o arquivo requirements.txt. Execute o seguinte comando no terminal:

pip install -r requirements.txt
Isso irá instalar todas as bibliotecas necessárias para o funcionamento do projeto.

Executando a API
Agora, você está pronto para executar a API. Para isso, execute o seguinte comando no terminal:

Navegue até o diretorio da API
cd caminho/dir/meu-dir
python app.py
Ou, caso esteja usando o Python 3 explicitamente:


cd caminho/dir/meu-dir
python3 app.py

A API será iniciada e estará disponível no endereço especificado (geralmente http://localhost:3000). Mude para porta da sua preferência

Executando o Script de Automação
Abra uma nova aba de terminal no mesmo diretório onde está o seu repositório.

Ative o ambiente virtual na nova aba, caso ainda não tenha feito:

Execute o script de automação que consome a API. No terminal, execute o seguinte comando:


python automation_script.py
Ou, caso esteja usando o Python 3 explicitamente:


python3 automation_script.py

Isso executará o script de automação que irá consumir a API, realizar o download dos arquivos, processá-los e preencher o formulário conforme os dados extraídos.

