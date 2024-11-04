import pandas as pd

class GerenciadorDeArquivos:
    def __init__(self, nome_arquivo):
        self.arquivo = pd.read_csv(nome_arquivo)
        self.path = nome_arquivo
        self.atualizar_arquivo()

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