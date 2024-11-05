from gerenciador_de_arquivos import GerenciadorDeArquivos

class Logs:
    def __init__(self):
        self.logs = GerenciadorDeArquivos('relatorios/logs.csv')
        self.relatorios = GerenciadorDeArquivos('relatorios/relatorio.csv')
    

    def log_emprestimo(self, cpf, isbn, quantidade):
        self.logs.adicionar_linha({'CPF': cpf, 'ISBN': isbn, 'Quantidade': quantidade, 'Tipo_de_atividade': 'Emprestimo'})
    
    def log_devolucao(self, cpf, isbn, quantidade):
        self.logs.adicionar_linha({'CPF': cpf, 'ISBN': isbn, 'Quantidade': quantidade, 'Tipo_de_atividade': 'Devolução'})
    
    def log_exclusao(self, motivo, isbn, quantidade):
        self.logs.adicionar_linha({'Motivo': motivo, 'ISBN': isbn, 'Quantidade': quantidade, 'Tipo_de_atividade': 'Exclusão'})