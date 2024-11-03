from gerenciador_de_arquivos import GerenciadorDeArquivos
class Livro:
    def __init__(self):
        self.estoque = GerenciadorDeArquivos('estoque/estoque.csv')

    def inserir(self):
        isbn = input('informe o ISBN: ')
        self.estoque.buscar_em_arquivo('isbn', isbn)

        if(isbn in self.estoque):
            quantidade = int(input('Esse livro já está cadastrado no sistema, por favor, informe a quantidade a ser adicionada: '))
            self.estoque.atualizar_livro(isbn, 'quantidade', self.estoque.buscar_em_arquivo('isbn', isbn)['quantidade'] + quantidade)
        else:
            produto = input('Informe o nome do livro: ')
            valor = float(input('Informe o valor do Livro: '))
            quantidade = int(input('Informe a quantidade: '))

            self.estoque.adicionar_linha({'isbn': isbn, 'nome': produto, 'quantidade': quantidade, 'valor': valor})

    def excluir(self):
        isbn = input('informe o ISBN: ')
        self.estoque.buscar_em_arquivo('isbn', isbn)

        if(isbn in self.estoque):
            quantidade = int(input('Informe a quantidade a ser removida: '))
            self.estoque.atualizar_livro(isbn, 'quantidade', self.estoque.buscar_em_arquivo('isbn', isbn)['quantidade'] -  quantidade)
        else:
            print('Livro nao cadastrado')