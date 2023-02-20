# E-commerce for Gamers

## Introdução

Esse projeto é uma API de um e-commerce de jogos, em que os gamers de todo o país poderão desfrutar dos melhores preços do mercado. 
Ela foi construída utilizando o Framework Django, Django Rest Framework,
o banco de dados Postgres e conteirizada com Docker.
Por se tratar apenas de uma API, este projeto **NÃO** inclui Front-end.


## Premissas

- Ter o Docker e Docker Compose instalados na máquina.
- Na raiz do projeto utilizar o comando: `docker-compose up --build`


## Configurações iniciais

**Todos os comandos a seguir precisam ser executados no terminal do container.**

**Comando para acessar terminal do container:**
```
docker exec -it e-commerce-games bash
```
  
- Rodar as migrates iniciais: Execute `python manage.py migrate` para que as bibliotecas padrões, arquivos estáticos sejam migrados para a base de dados. 

- Criar um superusuário: O super usuário será usado para acessar o Django Admin, presente em `localhost:8000/admin`. **Ainda estando no terminal do container** use o comando `python manage.py createsuperuser`. Com isso você deve fornecer um username e password, o email pode ser deixado em branco.

- Rodar as migrations das aplicações 'costumers' e 'products'.
  Utilize o comando `python manage.py makemigrations`, seguido do `python manage.py migrate`. Assim, os serviços presentes na API serão adicionados a base de dados.

- Carregar os dados para a base de dados: O comando `python manage.py loaddata products.json` irá carregar 12 produtos a base de dados, não precisando que o leitor precise cadastrar um produto de cada vez para testar.
  
Para verificar se tudo ocorreu como previsto, utilize o **username** e **password** cadastrados para o superuser e acesse `localhost:8000/admin/`
Verifique se o admin conta com a categoria de Clientes e Produtos. Verifique também se os 12 produtos foram cadastrados. 

**Para sair do terminal do container basta escrever `exit`**


## Endpoints

- `localhost:8000/`: Possui as rotas que serão usadas pela aplicação web.

- `localhost:8000/admin/`: Endpoint para a administração, para acessa-la basta utilizar o superuser criado nas Configurações Iniciais. Esse superuser poderá **APENAS** criar novos produtos para seu e-commerce, visto que informações de Compras e Clientes estão disponível apenas para visualização. 

- `localhost:8000/api/token/`: Endpoint com restrição ao método POST, receberá em seu corpo os atributos **username** e **password**, sendo estes o **email** e **senha** cadastrados em `localhost:8000/costumers/`. Retornará os tokens JWT **refresh** e **access** para serem usados no Postman ou Insomnia.

  **Obs**: Para Insomnia: Na aba "auth", selecione Bearer Token, com prefixo Bearer e o token obtido **SEM ASPAS**

- `localhost:8000/products/`: Possui a listagem completa dos produtos. Este endpoint só permite o método **"GET"**. No Viewset List, fornecido pelo Django Rest Framework, há o botão **Filtros**. Dentre os filtros, há ordenação dos produtos por Nome, preço e pontuação. Também tem filtros por preços maiores/menores que o valor informado. O campo Pesquisa, irá pesquisar o produto pelo Nome. 

- `localhost:8000/costumers/`: Esse endpoint lista todos os usuários cadastrados no sistema e também cria novos. Todos os campos mostrados no endpoint devem ser preenchidos para que o usuário possa se autenticar. 

  **Obs: O usuário cadastrado não possui permissão para entrar no admin**

- `localhost:8000/purchases/`: Esse endpoint é apenas para usuários autenticados. Para se autenticar olhe o endpoint `localhost:8000/api/token/` . Após estar autenticado, este endpoint irá listar todas as compras feitas por este usuário.

- `localhost:8000/purchases/pk/`: Esse endpoint receberá uma chave primária da compra de um usuário autenticado permitindo que tal objeto possa ser alterado. Uma alteração relevante está descrita em [examples/received.json](./examples/received.json)

- `localhost:8000/purchases/post_cart/`: Esse endpoint recebe apenas o método post. Ele é o responsável por receber o checkout do carrinho de compras vindo do Front-end. O modelo de envio do JSON está no diretório [examples/post_cart.json](./examples/post_cart.json).

  **Obs: Lembre-se que para fazer o post, o usuário precisa estar autenticado.**
  

## Bibliotecas utilizadas

- [Django](https://www.djangoproject.com/start/overview/)

- [Django Rest Framework](https://www.django-rest-framework.org/)

- [Django Filters](https://django-filter.readthedocs.io/en/stable/guide/usage.html): Filtros em `/products/`

- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/): Autenticação em `/api/token/`


## Considerações Finais

Como este projeto não inclui front-end, toda lógica para criar um carrinho dinâmico, se tornou inviável. A ideia construída em `/post_cart/` foi levando em consideração que a informação de carrinho do usuário seria armazenado em cache pela aplicação ou pelo navegador e o back-end teria acesso ao mesmo só depois da finalização da compra. Todas as verificações de preço e disponibilidade de produto foram verificadas novamente pelo Back-end afim de evitar conflitos.

Há alguns comentários, em inglês, pelo código, explicando um pouco o que cada método escrito e sobrescrito se propõe a fazer.


Obrigado pela atenção, gamer.****


## Contato

- [LinkedIn](https://www.linkedin.com/in/lucas-martins-caetano/)
- [Email](mailto:lucas.caetano@aluno.unievangelica.edu.br)
