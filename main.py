from livro import Livro

def escolherOperacao(self, operacao):
        match operacao:
            case 'INSERIR':
                self.inserir()
            case 'REMOVER':
                self.excluir()
            case 'LISTAR':
                self.listar()
            case 'SAIR':
                exit(1)


classeCompras = Livro()

while True:
    operacao = input('Escolha uma operação: INSERIR, REMOVER, LISTAR, SAIR: ')
    classeCompras.escolherOperacao(operacao)

