from livro_repository import LivroRepository
from logs import Logs

class Emprestimo:
    def __init__(self):
        self.livroRepository = LivroRepository()
        self.logs = Logs()
    def emprestar(self):
        isbn = int(input('informe o ISBN do livro:'))

        book, index = self.livroRepository.buscar_livro(isbn)

        if(book != None):
            cpf = input('informe o CPF do solicitante: ')
            quantidade = int(input('informe a quantidade de exemplares a serem emprestados: '))

            if(quantidade > book['Quantidade']):
                print('Quantidade maior que a existente, operação abortada')
                return
            else:
                self.livroRepository.atualizar({'index': index, 'Quantidade': book['Quantidade'] - quantidade})

                self.logs.log_emprestimo(cpf, isbn, quantidade)

                print('Livro emprestado com sucesso')
        else:
            print('Livro nao encontrado')

    def devolver(self):
        isbn = int(input('informe o ISBN do livro:'))

        book, index = self.livroRepository.buscar_livro(isbn)

        if(book != None):
            cpf = input('informe o CPF para a devolução: ')
            quantidade = int(input('informe a quantidade de exemplares a serem devolvidos: '))

            self.livroRepository.atualizar({'index': index, 'Quantidade': book['Quantidade'] + quantidade})

            self.logs.log_devolucao(cpf, isbn, quantidade)

            print('Livro devolvido com sucesso')
        else:
            print('Livro nao encontrado')