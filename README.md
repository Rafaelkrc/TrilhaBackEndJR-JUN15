![Código Certo Coders](https://utfs.io/f/3b2340e8-5523-4aca-a549-0688fd07450e-j4edu.jfif)

# 📚 Trilha Inicial BackEnd Jr
Este projeto tem como objetivo desenvolver uma API RESTful para gerenciamento de tarefas, proporcionando funcionalidades de CRUD (Create, Read, Update, Delete) de tarefas, autenticação de usuários e armazenamento dos dados em um banco de dados.

## Objetivos:
- Criar uma API que permita CRUD (Create, Read, Update, Delete) de tarefas.
- Implementar autenticação de usuários.
- Utilizar um banco de dados SQLite para armazenar as tarefas.
- Documentar todo o processo e apresentar as conclusões.

## Requisitos Funcionais:
- Criar Tarefa: Endpoint para criar uma nova tarefa.
- Listar Tarefas: Endpoint para listar todas as tarefas.
- Atualizar Tarefa: Endpoint para atualizar uma tarefa existente.
- Deletar Tarefa: Endpoint para deletar uma tarefa existente.

## Autenticação de Usuários:
- Registro de Usuário: Endpoint para registrar um novo usuário.
- Login de Usuário: Endpoint para autenticar um usuário e gerar um token JWT.
- Proteção de Rotas: Garantir que apenas usuários autenticados possam acessar os endpoints de tarefas.

## Banco de Dados:
- Utilizar SQLite como banco de dados para armazenar informações de usuários e tarefas.

   #### Estrutura do Projeto:
   ```plaintext
   project-root/
   │
   ├── src/
   │   ├── controllers/
   │   ├── models/
   │   ├── routes/
   │   ├── middlewares/
   │   ├── database/
   │   └── app.js
   │
   ├── .env
   ├── .gitignore
   ├── README.md
   └── package.json
   ```

# Gerenciador de Tarefas - API com Django Rest Framework

Esta é uma API simples para gerenciar tarefas, desenvolvida com Django Rest Framework. A API oferece endpoints para operações CRUD em tarefas. Possui ainda do registro de usuários e autenticação. O banco de dados utilizado é o SQLite.
Foi utilizado o python-decouple para gerenciar as váriaveis de ambiente, onde estas estão na pasta contrib/env-sample. Foi utilizados as views genericas do DRF o que facilitou na implementação da api e deixando o código limpo e feito o lint com o flake8.

## Como Configurar e Executar

### Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)

### Passos

1. Clone o repositório para a sua máquina local:
    ```bash
    git clone https://github.com/Rafaelkrc/TrilhaBackEndJR-JUN15.git
    cd TrilhaBackEndJR-JUN15
    ```

2. Crie um ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Para Windows use: venv\Scripts\activate
    ```

3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

4. Inclua um arquivo .env com as variáveis de ambiente:
    - Conforme definidas na pasta contrib/env-sample

5. Realize as migrações para criar as tabelas no banco de dados:
    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Endpoints Disponíveis

### 1. Registrar Usuário

- **Rota:** `api/v1/register/`
- **Método:** `POST`
- **Corpo da Requisição:**
    ```json
   {
      "username": "novousuario",
      "password": "senhaforte",
      "email": "usuario@example.com",
      "first_name": "Nome",
      "last_name": "Sobrenome"
   }
    ```

### 2. Login

- **Rota:** `api/v1/authentication/login/`
- **Método:** `POST`
- **Corpo da Requisição:**
    ```json
   {
      "username": "novousuario",
      "password": "senhaforte"
   }
    ```

### 3. Criar Tarefa

- **Rota:** `api/v1/todo/`
- **Método:** `POST`
- **Autenticação:** Token
- **Corpo da Requisição:**
    ```json
   {
      "id": 10,
      "task": "estudar para aprender",
      "created_at": "2024-08-13T17:50:47.218909-03:00",
      "do_in": "2024-08-10T12:00:00-03:00",
      "is_finished": false
   }
    ```

### 4. Listar Tarefas

- **Rota:** `/api/v1/todo/`
- **Método:** `GET`
- **Autenticação:** Token

### 5. Atualizar Tarefa

- **Rota:** `/api/v1/todo/{id}/`
- **Método:** `PUT`
- **Autenticação:** Token
- **Corpo da Requisição:**
    ```json
   {
      "task": "estudar para aprender",
      "created_at": "2024-08-06T15:15:16.824782-03:00",
      "do_in": "2024-08-10T12:00:00-03:00",
      "is_finished": true
   }
    ```

### 6. Deletar Tarefa

- **Rota:** `/api/v1/todo/{id}/`
- **Método:** `DELETE`
- **Autenticação:** Token

## Detalhes Técnicos

- **Banco de Dados:** SQLite
- **Autenticação:** Django Rest Framework com autenticação por jsonwebtoken (JWT), token expira em 1 dia.

## Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

