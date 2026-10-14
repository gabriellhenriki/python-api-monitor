# Python API Monitor

## Sobre o projeto

Projeto simples desenvolvido para praticar o consumo de uma API REST utilizando Python.

O programa consulta a API pública do GitHub e retorna informações de um usuário informado pelo usuário.

## Funcionalidades

- Consultar um usuário do GitHub
- Exibir nome
- Exibir nome de usuário (login)
- Exibir número de seguidores
- Exibir quantidade de repositórios públicos

## Tecnologias utilizadas

- Python 3
- Requests
- GitHub REST API

## Estrutura do projeto

```text
python-api-monitor/
├── main.py
├── api_client.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar

### 1. Clone o repositório

```bash
git clone <https://github.com/gabriellhenriki/python-api-monitor>
```

### 2. Entre na pasta do projeto

```bash
cd python-api-monitor
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o programa

```bash
python main.py
```

### 5. Digite o nome do usuário do GitHub quando solicitado

## Exemplo de uso

```text
Digite o nome do usuário no GitHub: torvalds

Nome: Linus Torvalds
Usuário: torvalds
Seguidores: 325972
Repositórios públicos: 12
```

## Autor

Desenvolvido por Gabriel Henrique como projeto de estudos para praticar consumo de APIs REST com Python.