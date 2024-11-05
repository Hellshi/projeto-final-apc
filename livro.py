from base_repository import BaseRepository
from livro_repository import LivroRepository
from logs import Logs
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
            quantidade = int(input(f"O livro {self.livro['Nome']} já está cadastrado no estoque com {self.livro['Quantidade']} itens. Informe a quantidade a ser adicionada: "))
            self.livro['Quantidade'] += quantidade
            self.livroRepository.atualizar(self.livro)
            print(f'Quantidade de {self.livro["Nome"]} atualizada para {self.livro["Quantidade"]}')
        else:
            self.livro['Nome'] = input('Informe o nome do livro: ')
            self.livro['Valor'] = float(input('Informe o valor do Livro: '))
            self.livro['Quantidade'] = int(input('Informe a quantidade: '))

            self.livroRepository.inserir(self.livro)

        self.logs.log_de_gestao_de_livros(None, self.livro['ISBN'], self.livro['Quantidade'], 'Inclusão')
        print(f'Livro {self.livro["Nome"]} adicionado ao estoque')

    def excluir(self):
        isbn = int(input('informe o ISBN: '))
        book, index = self.buscar_livro(isbn)
        
        if(book != None):
            quantidade = int(input('Informe a quantidade a ser removida: '))
            if(quantidade > book['Quantidade']):
                print('Quantidade maior que a existente, operação abortada')
                return
            else:
                motivo = input('Informe o motivo da exclusão: ')
                self.estoque.atualizar_livro(index, 'Quantidade', self.estoque.buscar_em_arquivo('ISBN', isbn)['Quantidade'] + quantidade)
                self.logs.log_de_gestao_de_livros(motivo, isbn, quantidade, 'Exclusão')
                print(f'Quantidade de {book["Nome"]} atualizada para {book["Quantidade"] - quantidade}')
        else:
            print('Livro nao cadastrado')
    
    def buscar_livro(self, isbn):
        item = self.estoque.buscar_em_arquivo('ISBN', isbn)

        if len(item) > 0:
            return [item.iloc[0].to_dict(), item.index[0]]
        else:
            return [None, None]
        
    def consultar(self):
        isbn = int(input('informe o ISBN: '))
        item = self.estoque.buscar_em_arquivo('ISBN', isbn)
        book = item.iloc[0]

        if(len(book) != None):
            print(book)
        else:
            print('Livro nao cadastrado')