from gerenciador_de_arquivos import GerenciadorDeArquivos
from logs import Logs


class Emprestimo:
    def __init__(self):
        self.estoque = GerenciadorDeArquivos('estoque/estoque.csv')
        self.logs = Logs()
    def emprestar(self):
        cpf = input('informe o CPF do solicitante: ')

        isbn = input('informe o ISBN do livro: ')

        quantidade = int(input('informe a quantidade de livros: '))

        self.estoque.atualizar_livro(isbn, 'quantidade', self.estoque.buscar_em_arquivo('isbn', isbn)['quantidade'] - quantidade)

        self.logs.log_emprestimo(cpf, isbn, quantidade)    
    def devolver(self):
        isbn = input('informe o ISBN do livro: ')

        quantidade = int(input('informe a quantidade de livros: '))

        self.estoque.atualizar_livro(isbn, 'quantidade', self.estoque.buscar_em_arquivo('isbn', isbn)['quantidade'] + quantidade)