import pandas as pd
from pandas.errors import EmptyDataError

class Relatorios_Repository:
    def __init__(self):
        self.estoquePath = './app/repository/estoque/estoque.csv'
        self.logsPath = './app/repository/relatorios/logs.csv'
        try:
            self.estoque = pd.read_csv(self.estoquePath, skip_blank_lines=True, header=0)
            self.logs = pd.read_csv(self.logsPath, skip_blank_lines=True, header=0)
        except EmptyDataError:
            self.estoque = pd.DataFrame()
            self.logs = pd.DataFrame()
    
    def livros_mais_populares(self):
        self.estoque = self.estoque.drop(columns=["Quantidade"])

        self.logs = self.logs.drop(columns=["Motivo", "CPF"])
        
        mergedData = self.mergeData()

        df_emprestimos = mergedData[mergedData["Tipo_de_atividade"] == "Emprestimo"]

        livros_mais_emprestados = df_emprestimos.groupby(["ISBN", "Nome"])["Quantidade"].sum()

        livros_mais_emprestados = livros_mais_emprestados.sort_values(ascending=False).reset_index()

        return livros_mais_emprestados

    def mergeData(self):
        mergedData = pd.merge(self.estoque, self.logs, on="ISBN", how="left")

        return mergedData
