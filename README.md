# API MoreU

API feita para estudos do projeto da faculdade com o intuito de realizar o controle de ativos de uma empresa (Cliente)

## Objetivos do Case:

- Gerar relatório de um controle de ativos
- Monitoramento em tempo real dos ativos da empresa
- Obter e adicionar informações de ativos da empresa 

## Funcionalidades do Case:

- Usuário deve gerar registro de ativos da empresa
- Usuário poderá utilizar todas as operações CRUD no sistema
- Usuário poderá filtrar informações e gerar relatórios a partir delas

## Funcionalidades não implementadas

- Sistema de login e autenticação

## Macro funcionalidades

- Sistema CRUD completo e semântico 
- Restful API utilizando ORM 

## Stack

![Stack](https://img.shields.io/badge/python-f7d44c?logo=python&logoColor=2f6592&style=for-the-badge) ![Stack](https://img.shields.io/badge/Flask-black?logo=flask&logoColor=white&style=for-the-badge) ![Stack](https://img.shields.io/badge/sqlachemy-d31c00?logo=sqlalchemy&logoColor=white&style=for-the-badge)  ![Stack](https://img.shields.io/badge/mysql-5a839c?logo=mysql&logoColor=white&style=for-the-badge) ![Stack](https://img.shields.io/badge/git-e05d44?logo=git&logoColor=white&style=for-the-badge)



## Instalação

Para realizar a instalação, primeiro, clone o repositório em sua máquina:

### Clonando o repositório

```
git clone https://github.com/AntonioALino/API_MoreU.git
```

Acesse a pasta:

```
cd API_MoreU
```

### Configurando o ambiente

Agora, iremos criar um ambiente de desenvolvimento python com o seguinte comando:

```
python -m venv .venv
```

Então vamos acessar esse ambiente que acabamos de criar:

```
source .venv/bin/activate
```

Vamos também instalar todas as dependências:

```
pip install -r requirements.txt
```

Também importe o arquivo ```dump.sql``` em seu servidor MySQL.


Por fim, você precisará criar/editar o arquivo ```.env``` presente na raiz do projeto, adicionando suas credenciais de conexão com o banco de dados:

```env
URL=mysql+mysqlconnector://usuário do banco:senha do banco@servidor do banco/moreu
```

Pronto! O projeto está pronto para ser testado!


## Testando

Execute o código em seu editor favorito, ou rode o seguinte comando no terminal:

```
flask --app main.py
```

Você também pode testar online, com uma interface gráfica acessando o seguinte link:

https://moreu-frontend.vercel.app


## Modelo Relacional e lógico


Modelo Relacional:

![Modelo Relacional](docs/relational_model.png)


Modelo Lógico:

![Modelo Relacional](docs/logic_model.png)
