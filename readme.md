# Literatura: 
Motivação: Um projeto simples para gestão da sua biblioteca via terminal, ele utilizará conceitos básicos de python para desenvolver um sistema de acervo, empréstimo e compras de livros para uma biblioteca qualquer.

## Regras de Negócio:
- Adição de livros:
    - Para que um livro seja adicionado ele deve possuir as seguintes caracteristicas: 

    | Nome               | Valor  | ISBN          | Quantidade |
    |--------------------|--------|---------------|------------|
    | A Metamorfose      | 29.90  | 9783161484100 | 15         |
    | O Senhor dos Anéis | 59.90  | 9780062024022 | 8          |
    
    - Os livros podem ser adicionados ao estoque em lotes através do campo "quantidade";
    
- Deleção de livro:
    - Ao deletar um livro deve ser informado o motivo da remoção daquele(s) volumes. O informe deve ser uma string. Esse informe será exibido posteriormente nos relatórios;

- Empréstimo de livros: 
    - Os livros podem ser tomados emprestados por indivíduo qualquer.
    - Ao tomar emprestado o livro, deve ser informado o cpf de quem está tomando emprestado

- Devolução:
    - Ao devolver um livro deve ser informado o código ISBN dele e o livro deve voltar imediatamente ao estoque
- Relatórios: 
Os relatórios podem ser encontrados na raíz do projeto e tem nomes correspondentes ao seu tipo. Eles tem por objetivo facilitar a tomada de decisões logisticas para o sucesso da livraria
    - O usuário pode vizualizar relatórios de:
        - Livros Mais populares:
            - definido pela quantidade de empréstimos daquele livro
        - Livros deletados
            - Mostra o motivo da remoção de uma quantidade x de exemplares do livro
        - Estoque de livros
            - Mostra o estoque de cada livro cadastrado no sistema