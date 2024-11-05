from InquirerPy import inquirer

from app.emprestimo import Emprestimo
from app.livro import Livro
from app.relatorios import Relatorios


options = ["Emprestimo", "Gestão de Livros", "Relatórios", "Sair"]
gestao_de_livros_options = ["Inseririr Livro", "Excluir Livro", "Buscar Livro", "Sair"]
emprestimo_options = ["Emprestar Livro", "Devolver Livro", "Sair"]
relatorios_options = ["Livros Mais Populares", "Livros deletados", "Estoque de Livros", "Sair"]

class Main:
    def __init__(self):
        self.livro = Livro()
        self.emprestar = Emprestimo()
        self.relatorio = Relatorios()

    def gestao_de_livros(self):
        bookOptions = {
            "Inseririr Livro": self.livro.inserir,
            "Excluir Livro": self.livro.excluir,
            "Buscar Livro": self.livro.consultar
        }
        selected_option = inquirer.select(
            message="Escolha uma opção:",
            choices=gestao_de_livros_options
        ).execute()

        bookOptions[selected_option]()
    
    def emprestimo(self):
        emprestimo = {
            "Emprestar Livro": self.emprestar.emprestar,
            "Devolver Livro": self.emprestar.devolver,
        }
        selected_option = inquirer.select(
            message="Escolha uma opção:",
            choices=emprestimo_options
        ).execute()

        emprestimo[selected_option]()
    
    def relatorios(self):
        selected_option = inquirer.select(
            message="Escolha uma opção:",
            choices=relatorios_options
        ).execute()

        if selected_option == "Livros Mais Populares":
            self.relatorio.livros_mais_populares()
    
    def exit(self):
        print("Saindo...")
        exit()
        


while True:
    selected_option = inquirer.select(
        message="Escolha uma opção:",
        choices=options
    ).execute()

    options = {
        "Emprestimo": Main().emprestimo,
        "Gestão de Livros": Main().gestao_de_livros,
        "Relatórios": Main().relatorios,
        "Sair": Main().exit
    }

    options[selected_option]()