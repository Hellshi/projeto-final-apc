

from app.repository.relatorios_repository import Relatorios_Repository
import pandas as pd

class Relatorios:
    def __init__(self):
        self.relatorioRepository = Relatorios_Repository()
    
    def livros_mais_populares(self):
        results = self.relatorioRepository.livros_mais_populares()
        print(results)
        results.to_csv("livros_mais_emprestados.csv", index=False)
