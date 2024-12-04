
# Desafio: Teste Desenvolvedor Python - Golden Raspberry Awards API

Desenvolva uma API RESTful para possibilitar a leitura da lista de indicados e vencedores da categoria Pior Filme do Golden Raspberry Awards.

## Requisito do sistema

Ler o arquivo CSV dos filmes e inserir os dados em uma base de dados ao iniciar a aplicação.

## Requisitos da API

Obter o produtor com maior intervalo entre dois prêmios consecutivos, e o que obteve dois prêmios mais ápido, seguindo a especificação de formato definida na página 2;

## Requisitos não funcionais do sistema

1. O web service RESTful deve ser implementado com base no nível 2 de maturidade de Richardson;

2. Devem ser implementados somente testes de integração. Eles devem garantir que os dados obtidos estão de acordo com os dados fornecidos na proposta;

3. O banco de dados deve estar em memória utilizando um SGBD embarcado (por exemplo, H2). Nenhuma instalação externa deve ser necessária;

4. A aplicação deve conter um readme com instruções para rodar o projeto e os
testes de integração.

### Passos para Instalação

**1. Clonar o repositório:**

```
git clone https://github.com/pericacs/desafio_tec_back_outsera.git
cd desafio_tec_back_outsera
```

**2. Criar um ambiente virtual (opcional, mas recomendado):**

```
python -m venv venv
venv\Scripts\activate  # Para Windows
```
**3. Instalar as dependências**: As dependências do projeto estão listadas no arquivo requirements.txt. Para instalá-las, execute:

```
pip install -r requirements.txt
```
**4. Execute a aplicação**: 

```
python app.py
```

**5. Acessar API**: Acesse a API no endereço: [http://127.0.0.1:5000/producers/intervals](http://127.0.0.1:5000/producers/intervals).


### Testes

Para rodar os testes de integração:

```
pytest test_app.py
```
