# Exemplos 

## post_cart.json

Esse modelo deve ser usado no corpo da requisição, juntamente com a autenticação do usuário. 

- product: primary key do produto
- quantity: Quantidade do produto

**Sugestão: Os produtos de pk's = 10, 11 e 12 possuem pouca quantidade em estoque. Foram criados para testar o que acontece quando um cliente tenta comprar uma quantidade maior do que há na base de dados.**


## received.json

**PATCH `localhost:8000/purchases/pk/`**

Alterando tal atributo, uma lógica irá acrescentar o dia e a hora do momento atual aos dados da Compra. 