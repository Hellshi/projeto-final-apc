from InquirerPy import inquirer
from livro import Livro

options = ["Emprestimo", "Gestão de Livros", "Relatórios", "Sair"]

while True:
    selected_option = inquirer.select(
        message="Escolha uma opção:",
        choices=options
    ).execute()

    if selected_option == "Emprestimo":
        print("Emprestimo")
    elif selected_option == "Gestão de Livros":
        Livro().inserir()
    elif selected_option == "Relatórios":
        print("Relatórios")

    print("Opção selecionada:", selected_option)
    
    # Encerra o loop se a opção "Sair" for selecionada
    if selected_option == "Sair":
        print("Encerrando o programa.")
        break