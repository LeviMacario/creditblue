<img src="https://www.onidata.com/img/logo-rodape.jpg" width="127px" align="left"/>

# Credit Blue

[Acesse nosso site! ;)](https://www.onidata.com)

<br>

API Rest para contratos de empréstimos
<br>


## Índice

- [Introdução](#introdução)
- [Tecnologia utilizada](#tecnologia-utilizada)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Estrutura do projeto](#estrutura-do-projeto)

## Introdução 

Credit Blue é uma plataforma que tem como objetivo, proporcionar um controle de contratos de empréstimos através de uma API Rest.

## Tecnologia utilizada

A stack foi escolhida com base no que empresas grandes estão usando para construir suas experiências.
Também foi levado em consideração a simplicidade, curva de aprendizado e requisitos
como fácil distribuição e entrega rápida.

Tendo isso em vista, optamos por usar [Python 3](https://www.python.org/), [Django](https://www.djangoproject.com/), [Django Rest Framework](https://www.django-rest-framework.org/) e [PostgreSQL](https://www.postgresql.org/).

## Requisitos

Este repositório é um monorepo que aloja os pacotes que compõem o Credit Blue.
Para instalar as dependências é necessário usar o [pip](https://pypi.org/project/pip/).

## Instalação

Algumas instruções para desenvolver no Credit Blue:

1. **Clonando o repositório**

	```sh
	$ git clone git@github.com:LeviMacario/creditblue.git
	```

2. **Rodando o servidor**

	Entre na pasta principal do projeto:

	```sh
	$ cd creditblue
	```

    Crie o ambiente virtual (Virtualenvwrapper)
    ```sh
    $ mkvirtualenv -p python3 creditblue
    ```

    Acesse o ambiente virtual
    ```sh
    $ workon creditblue
    ```

    Crie uma cópia de .env.example para .env (Esse arquivo é necessário para carregar as variáveis de ambiente):

	```sh
	$ cp .env.example .env
	```

    Crie um banco de dados "creditblue" com usuário "creditblue" e senha "12345" no postgres(Pode usar o pgAdmin):


    Instalação das dependências, criação das tabelas e população do banco de dados:

	```sh
	$ make setup
	```

	Inicie a aplicação (em ambiente de desenvolvimento):

	```sh
	$ make run
	```

3. **Acessando a Administração do sistema**

    1. Acesse: http://localhost:8000/admin
    2. Entre com usuário: admin@creditblue.com e senha: @123456!

## Estrutura do projeto

- **`creditblue`**: Toda a estrutura de arquivos e pastas do projeto.
    - **`core`**: App central para auxiliar as demais apps.
    - **`contracts`**: App responsável pelos contratos de empréstimos e pagamentos.
    - **`financial`**: App responsável pelos bancos.
    - **`customers`**: App responsável pelos clientes que contratam empréstimos.
    - **`api`**: App responsável pela api do projeto.
    - **`creditblue`**: App raiz do projeto onde localiza-se o settings.py.
    - **`users`**: App responsável pelos usuários.
    - **`manage.py`**: Arquivo principal para Django executar tarefas.
    - **`.gitignore`**: Arquivo responsável pelas exceções do repositório git.
    - **`requirements.txt`**: Arquivo que guarda todas as dependências do projeto.
    - **`README.md`**: Arquivo que possui as instruções para uso do projeto.
    - **`Makefile`**: Arquivo que possui tasks automatizadas do projeto.
    - **`.env.example`**: Arquivo que possui as variáveis de ambiente de desenvolvimento do projeto.
    