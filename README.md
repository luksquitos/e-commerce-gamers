# E-commerce for Gamers

## Introdução

Esse projeto é uma API de um e-commerce de jogos, em que os gamers de todo o país poderão desfrutar dos melhores preços. 
Ela foi construída utilizando o Framework Django, Django Rest Framework,
o banco de dados Postgres e conteirizada com Docker.
Por se tratar apenas de uma API, este projeto **NÃO** inclui Front-end.

## Premissas

- Ter o Docker e Docker Compose instalados na máquina.
- Na raiz do projeto utilizar o comando: `docker-compose up --build`

## Configurações iniciais

**Todos os comandos a seguir precisam ser executados no terminal do container.**

- **Comando para acessar terminal do container: `docker-compose exec -it e-commerce-games bash`**
  
- Rodar as migrates iniciais: Execute `python manage.py migrate` para que as bibliotecas padrões, arquivos estáticos sejam migrados para a base de dados. 

- Criar um superusuário: O super usuário será usado para acessar o Django Admin, presente em `localhost:8000/admin`. **Ainda estando no terminal do container** use o comando `python manage.py createsuperuser`. Com isso você deve fornecer um username e password, o email pode ser deixado em branco.

- Rodar as migrations das aplicações 'costumers' e 'products'.
  Utilize o comando `python manage.py makemigrations`, seguido do `python manage.py migrate`. Assim, os serviços presentes na API serão adicionados a base de dados.

- Carregar os dados para a base de dados: O comando `python manage.py loaddata products.json` irá carregar 12 produtos a base de dados, não precisando que o leitor precise cadastrar um produto de cada vez para testar.
  
Para verificar se tudo ocorreu como previsto, utilize o **username** e **password** cadastrados para o superuser e acesse `localhost:8000/admin`
Verifique se o admin conta com a Categoria de Clientes e Produtos. Verifique também se há 12 produtos cadastrados. 

**Para sair do terminal do container basta escrever `exit`**

## Endpoints
- `localhost:8000/`: Possui as rotas que serão usadas pela aplicação web.
- `localhost:8000/products/`: Possui a listagem completa dos produtos. Este endpoint só permite o método **"GET"**. No Viewset List, fornecido pelo Django Rest Framework, há o botão **Filtros**. Dentre os filtros, há ordenação dos produtos por Nome, preço e pontuação. Também tem filtros por preços maiores/menores que o valor informado. O campo Pesquisa, irá pesquisar o produto pelo Nome. 
- `localhost:8000/costumers/`

## Bibliotecas utilizadas

## Contato