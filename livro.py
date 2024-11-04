from gerenciador_de_arquivos import GerenciadorDeArquivos
class Livro:
    def __init__(self):
        self.estoque = GerenciadorDeArquivos('estoque/estoque.csv')

    def inserir(self):
        isbn = int(input('informe o ISBN: '))
        book, index = self.buscar_livro(isbn)

        if(book != None):
            quantidade = int(input(f"O livro {book['Nome']} já está cadastrado no estoque com {book['Quantidade']} itens. Informe a quantidade a ser adicionada: "))
            self.estoque.atualizar_livro(index, 'Quantidade', self.estoque.buscar_em_arquivo('ISBN', isbn)['Quantidade'] + quantidade)
        else:
            produto = input('Informe o nome do livro: ')
            valor = float(input('Informe o valor do Livro: '))
            quantidade = int(input('Informe a quantidade: '))

            self.estoque.adicionar_linha({'ISBN': isbn, 'Nome': produto, 'Quantidade': quantidade, 'Valor': valor})

    def excluir(self):
        isbn = input('informe o ISBN: ')
        self.estoque.buscar_em_arquivo('isbn', isbn)

        if(isbn in self.estoque):
            quantidade = int(input('Informe a quantidade a ser removida: '))
            self.estoque.atualizar_livro(isbn, 'quantidade', self.estoque.buscar_em_arquivo('isbn', isbn)['quantidade'] -  quantidade)
        else:
            print('Livro nao cadastrado')
    
    def buscar_livro(self, isbn):
        item = self.estoque.buscar_em_arquivo('ISBN', isbn)
        if len(item) > 0:
            return [item.iloc[0].to_dict(), item.index[0]]
        else:
            return