# Trabalho de Formula 1
Projeto final da disciplina Laboratório de Base de Dados


## Como preparar o ambiente
### Banco de dados
 Primeiramente, precisamos configurar o banco de dados.
 O primeirio passo é realizar a carga dos dados que estão contidos nos arquivos disponibilizados. Essa carga é a mesma fornecida pelo professor no T1.
 > Execute o arquivo ./queries/carga_bd.sql no pgAdmin
 
 Depois vamos criar as tabelas de usuários e logs. Então, por favor
 > Execute o arquivo ./queries/users.sql no pgAdmin

 E então 
 > Execute o arquivo ./queries/setup_R2.sql

 Para preparar o ambiente para o relatorio 2.

 Após isso o banco de dados estará pronto para uso.

### Python
Para criar a API utilizamos o framework FastAPI, que permite criar APIs rapidamente. Para interagir com o banco de dados foi utilizada a lib de python PyODBC, que NÃO é um ORM. Para utilizar a API vamos precisar instalar alguns pacotes então é recomendado que se crie um ambiente virtual.

[Tutorial disponível clicando aqui.](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv)

#### Dependencias
Instale as dependencias com os comandos abaixo:
>pip install "fastapi[all]"

>pip install pyodbc

>pip install python-dotenv

## Como usar
No terminal, ative a API com o comando
> uvicorn main:app --reload

e vá até o link http://127.0.0.1:8000/docs , onde você poderá testar a API

## Como funciona
Na raiz da pasta há 6 arquivos python:

admin.py - Armazena as funções de um Adminstrador
database.py - Responsável por conectar a API ao banco de dados e realizar queries
escuderia.py - Agrega as funções e o modelo das escuderias
login.py - Armazena a função de login e permite acesso às outras funções
main.py - Responsável por rodar a API
piloto.py - Armazena as funções do piloto

