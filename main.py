from InquirerPy import inquirer
from livro import Livro

options = ["Emprestimo", "Gestão de Livros", "Relatórios", "Sair"]
gestao_de_livros_options = ["Inseririr Livro", "Excluir Livro", "Buscar Livro", "Sair"]

class Main:
    def __init__(self):
        self.livro = Livro()

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
        


while True:
    selected_option = inquirer.select(
        message="Escolha uma opção:",
        choices=options
    ).execute()

    if selected_option == "Gestão de Livros":
        print("Entrou")
        Main().gestao_de_livros()

    if selected_option == "Sair":
        print("Encerrando o programa.")
        break