from gerenciador_de_arquivos import GerenciadorDeArquivos


class Emprestimo:
    def __init__(self):
        self.estoque = GerenciadorDeArquivos('estoque/estoque.csv')

    def emprestar(self):
        cpf = input('informe o CPF do solicitante: ')

        isbn = input('informe o ISBN do livro: ')

        quantidade = int(input('informe a quantidade de livros: '))

        self.estoque.atualizar_livro(isbn, 'quantidade', self.estoque.buscar_em_arquivo('isbn', isbn)['quantidade'] - quantidade)
    
    def devolver(self):
        isbn = input('informe o ISBN do livro: ')

        quantidade = int(input('informe a quantidade de livros: '))

        self.estoque.atualizar_livro(isbn, 'quantidade', self.estoque.buscar_em_arquivo('isbn', isbn)['quantidade'] + quantidade)