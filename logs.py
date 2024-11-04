from gerenciador_de_arquivos import GerenciadorDeArquivos

class Logs:
    def __init__(self):
        self.relatorios = GerenciadorDeArquivos('relatorios/relatorios.csv')
    

    def log_emprestimo(self, cpf, isbn, quantidade):
        self.relatorios.adicionar_linha({'cpf': cpf, 'isbn': isbn, 'quantidade': quantidade, 'tipo_de_atividade': 'Emprestimo'})