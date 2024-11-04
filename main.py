from InquirerPy import inquirer

options = ["Opção 1", "Opção 2", "Opção 3", "Sair"]

while True:
    selected_option = inquirer.select(
        message="Escolha uma opção:",
        choices=options
    ).execute()

    print("Opção selecionada:", selected_option)
    
    # Encerra o loop se a opção "Sair" for selecionada
    if selected_option == "Sair":
        print("Encerrando o programa.")
        break