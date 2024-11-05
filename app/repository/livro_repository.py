
from app.repository.base_repository import BaseRepository

class LivroRepository(BaseRepository):
    def __init__(self):
        super().__init__('app/repository/estoque/estoque.csv')
    
    def inserir(self, livro):
        print(livro)
        self.adicionar_linha({'ISBN': livro['ISBN'], 'Nome': livro['Nome'], 'Quantidade': livro['Quantidade'], 'Valor': livro['Valor']})

    def atualizar(self, livro):
        self.atualizar_livro(livro['index'], 'Quantidade', livro['Quantidade'])

    def remover(self, livro):
        self.atualizar_livro(livro['index'], 'Quantidade', self.buscar_em_arquivo('ISBN', livro['ISBN'])['Quantidade'] - livro['Quantidade'])

    def buscar_livro(self, isbn):
        item = self.buscar_em_arquivo('ISBN', isbn)

        if len(item) > 0:
            return [item.iloc[0].to_dict(), item.index[0]]
        else:
            return [None, None]

    def consultar(self, isbn):
        item = self.buscar_em_arquivo('ISBN', isbn)
        return item.iloc[0]