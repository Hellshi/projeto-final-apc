from gerenciador_de_arquivos import GerenciadorDeArquivos

class Logs:
    def __init__(self):
        self.relatorios = GerenciadorDeArquivos('relatorios/relatorios.csv')
    

    def log_de_atividade(self, tipo_de_atividade, isbn, quantidade):
        self.relatorios.adicionar_linha({'tipo_de_atividade': tipo_de_atividade, 'isbn': isbn, 'quantidade': quantidade})