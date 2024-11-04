import pandas as pd

class GerenciadorDeArquivos:
    def __init__(self, nome_arquivo):
        self.arquivo = pd.read_csv(nome_arquivo)
        "self.atualizar_arquivo()"

    def atualizar_arquivo(self):
        self.arquivo.to_csv(self.arquivo, index=False)
    
    def adicionar_linha(self, linha):
        self.arquivo = self.arquivo.append(linha, ignore_index=True)
        self.atualizar_arquivo()
    
    def exibir_arquivo(self):
        print(self.arquivo)
    
    def buscar_em_arquivo(self, coluna, valor):
        item = self.arquivo.loc[self.arquivo[f"{coluna}"] == valor]
        if len(item) > 0:
            return item.iloc[0].to_dict()
        else:
            return
    
    def atualizar_livro(self, linha, coluna, valor):
        self.arquivo.at[linha, coluna] = valor
        self.atualizar_arquivo()