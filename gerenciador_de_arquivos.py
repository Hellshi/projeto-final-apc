import pandas as pd
from pandas.errors import EmptyDataError

class GerenciadorDeArquivos:
    def __init__(self, nome_arquivo):
        try:
            self.arquivo = pd.read_csv(nome_arquivo, skip_blank_lines=True, header=0)
            self.path = nome_arquivo
        except EmptyDataError:
            self.arquivo = pd.DataFrame()
            self.path = nome_arquivo

    def atualizar_arquivo(self):
        self.arquivo.to_csv(self.path, index=False)
    
    def adicionar_linha(self, linha):
        nova_linha_df = pd.DataFrame([linha])
        self.arquivo = pd.concat([self.arquivo, nova_linha_df], ignore_index=True)
        self.atualizar_arquivo()
    
    def exibir_arquivo(self):
        print(self.arquivo)
    
    def buscar_em_arquivo(self, coluna, valor):
        return self.arquivo.loc[self.arquivo[f"{coluna}"] == valor]

    def atualizar_livro(self, linha, coluna, valor):
        self.buscar_em_arquivo(coluna, linha)
        self.arquivo.at[linha, coluna] = valor
        self.atualizar_arquivo()