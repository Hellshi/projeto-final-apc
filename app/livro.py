
from app.repository.livro_repository import LivroRepository
from app.repository.logs import Logs
class Livro:
    def __init__(self):
        self.livroRepository = LivroRepository()
        self.logs = Logs()
        self.livro = {
            'ISBN': None,
            'Nome': None,
            'Quantidade': None,
            'Valor': None,
            'index': None
        }

    def inserir(self):
        isbn = int(input('informe o ISBN: '))
        book, index = self.livroRepository.buscar_livro(isbn)
        self.livro = {'ISBN': isbn, 'Nome': None, 'Quantidade': None, 'Valor': None, 'index': index}

        if(book != None):
            self.livro['Quantidade'] = book['Quantidade']
            self.livro['Nome'] = book['Nome']
            self.livro['Valor'] = book['Valor']
            self.livro['index'] = index
            self.atualizar()
        else:
            self.livro['Nome'] = input('Informe o nome do livro: ')
            self.livro['Valor'] = float(input('Informe o valor do Livro: '))
            self.livro['Quantidade'] = int(input('Informe a quantidade: '))

            self.livroRepository.inserir(self.livro)

        self.logs.log_de_gestao_de_livros(None, self.livro['ISBN'], self.livro['Quantidade'], 'Inclusão')
        print(f'Livro {self.livro["Nome"]} adicionado ao estoque')

    def excluir(self):
        isbn = int(input('informe o ISBN: '))
        book, index = self.livroRepository.buscar_livro(isbn)
        
        if(book != None):
            quantidade = int(input('Informe a quantidade a ser removida: '))
            if(quantidade > book['Quantidade']):
                print('Quantidade maior que a existente, operação abortada')
                return
            else:
                self.livro['Quantidade'] = quantidade
                self.livro['ISBN'] = book['ISBN']
                self.livro['index'] = index

                motivo = input('Informe o motivo da exclusão: ')
                self.livroRepository.remover(self.livro)
                
                self.logs.log_de_gestao_de_livros(motivo, isbn, book['Quantidade'] - quantidade, 'Exclusão')
                print(f'Quantidade de {book["Nome"]} atualizada para {book["Quantidade"] - quantidade}')
        else:
            print('Livro nao cadastrado')
    
    def atualizar(self):
        quantidade = int(input(f"O livro {self.livro['Nome']} já está cadastrado no estoque com {self.livro['Quantidade']} itens. Informe a quantidade a ser adicionada: "))
        self.livro['Quantidade'] += quantidade
        self.livroRepository.atualizar(self.livro)
        print(f'Quantidade de {self.livro["Nome"]} atualizada para {self.livro["Quantidade"]}')
        
    def consultar(self):
        isbn = int(input('informe o ISBN: '))
        book = self.livroRepository.consultar(isbn)
    
        if(len(book) != None):
            print(book)
        else:
            print('Livro nao cadastrado')