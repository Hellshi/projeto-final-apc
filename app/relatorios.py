

from app.repository.relatorios_repository import Relatorios_Repository
import pandas as pd

class Relatorios:
    def __init__(self):
        self.relatorioRepository = Relatorios_Repository()
    
    def livros_mais_populares(self):
        results = self.relatorioRepository.livros_mais_populares()
        results.to_csv("livros_mais_emprestados.csv", index=False)
    
    def exemplares_excluidos(self):
        results = self.relatorioRepository.exemplares_excluidos()
        results.to_csv("exemplares_excluidos.csv", index=False)
    
    def estoque(self):
        results = self.relatorioRepository.relatorio_de_estoque()
        results.to_csv("estoque.csv", index=False)
