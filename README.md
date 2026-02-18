# API de Carros

Esta é uma API RESTful simples desenvolvida para fins de estudo sobre a criação de APIs com Python, utilização do framework Flask e integração com banco de dados SQLite.

A aplicação permite gerenciar um catálogo de carros, oferecendo funcionalidades para listar, buscar, adicionar e remover veículos.

## Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **Flask**: Micro-framework web para construção da API.
*   **SQLite**: Banco de dados relacional leve e embutido.

## Como Executar o Projeto

1.  **Clone o repositório:**

    ```bash
    git clone <url-do-repositorio>
    cd <nome-do-diretorio>
    ```

2.  **Crie e ative um ambiente virtual (opcional, mas recomendado):**

    *   No Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    *   No Linux/macOS:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**

    ```bash
    python app.py
    ```

    A API estará rodando em `http://127.0.0.1:5000`. O banco de dados `cars_api.db` será criado automaticamente com alguns dados iniciais se não existir.

## Endpoints da API

### Listar todos os carros

Retorna uma lista com todos os carros cadastrados.

*   **URL:** `/carros`
*   **Método:** `GET`
*   **Resposta de Sucesso (200 OK):**
    ```json
    [
        {
            "id": 1,
            "nome": "Fiat Marea Turbo",
            "ano": "1999",
            "estilo": "Sedan",
            "tracao": "FWD"
        },
        ...
    ]
    ```

### Buscar carro por ID

Retorna os detalhes de um carro específico.

*   **URL:** `/carros/<id>`
*   **Método:** `GET`
*   **Parâmetros de URL:** `id` (Inteiro)
*   **Resposta de Sucesso (200 OK):**
    ```json
    {
        "id": 1,
        "nome": "Fiat Marea Turbo",
        "ano": "1999",
        "estilo": "Sedan",
        "tracao": "FWD"
    }
    ```
*   **Resposta de Erro (404 Not Found):**
    ```json
    {
        "error": "Carro não encontrado"
    }
    ```

### Adicionar um novo carro

Cadastra um novo carro no banco de dados.

*   **URL:** `/carros`
*   **Método:** `POST`
*   **Corpo da Requisição (JSON):**
    ```json
    {
        "nome": "Nome do Carro",
        "ano": "Ano",
        "estilo": "Estilo",
        "tracao": "Tração"
    }
    ```
    *Todos os campos são obrigatórios.*

*   **Resposta de Sucesso (201 Created):**
    ```json
    {
        "message": "Carro adicionado com sucesso!"
    }
    ```
*   **Resposta de Erro (400 Bad Request):**
    ```json
    {
        "error": "Todos os campos são obrigatórios"
    }
    ```

### Remover um carro

Remove um carro do banco de dados pelo seu ID.

*   **URL:** `/carros/<id>`
*   **Método:** `DELETE`
*   **Parâmetros de URL:** `id` (Inteiro)
*   **Resposta de Sucesso (200 OK):**
    ```json
    {
        "message": "Carro removido com sucesso!"
    }
    ```

## Estrutura do Projeto

*   `app.py`: Arquivo principal contendo as rotas e a inicialização da aplicação Flask.
*   `database.py`: Módulo responsável pela conexão com o banco de dados e funções de CRUD (Create, Read, Update, Delete).
*   `cars_api.db`: Arquivo do banco de dados SQLite (gerado automaticamente).
*   `requirements.txt`: Lista de dependências do projeto.
