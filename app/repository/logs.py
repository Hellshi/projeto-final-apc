
from app.repository.base_repository import BaseRepository

class Logs(BaseRepository):
    def __init__(self):
        super().__init__('app/repository/relatorios/logs.csv')

    def log_emprestimo(self, cpf, isbn, quantidade):
        self.adicionar_linha({'CPF': cpf, 'ISBN': isbn, 'Quantidade': quantidade, 'Tipo_de_atividade': 'Emprestimo'})
    
    def log_devolucao(self, cpf, isbn, quantidade):
        self.adicionar_linha({'CPF': cpf, 'ISBN': isbn, 'Quantidade': quantidade, 'Tipo_de_atividade': 'Devolução'})
    
    def log_de_gestao_de_livros(self, motivo, isbn, quantidade, tipo):
        self.adicionar_linha({'Motivo': motivo, 'ISBN': isbn, 'Quantidade': quantidade, 'Tipo_de_atividade': tipo})