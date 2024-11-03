#matrícula: 202435058
class Livro:
    def __init__(self):
        self._compras = []
        self.estoque = {}

    def inserir(self):
        produto = input('Informe o nome do produto: ')
        valorUnitario = float(input('Informe o valor unitário: '))
        quantidade = int(input('Informe a quantidade: '))
        self.estoque[produto] = {
            'quantidade': quantidade,
            'valorUnitario': valorUnitario
        }

    def excluir(self):
        produto = input('informe o nome do produto: ')
        if not produto in self.estoque:
            print("Produto não encontrado!")
            return
        
        del self.estoque[produto]
        print("Produto excluido com sucesso!")
    
    def listar(self):
        produtos = self.estoque.keys()
        total = 0
        for i in produtos:
            produto = self.estoque[i]
            totalEstoque = produto['quantidade'] * produto['valorUnitario']

            print("{} {} x R${:.2f} = R${:.2f}".format(i, produto['quantidade'], produto['valorUnitario'], totalEstoque))
            total += totalEstoque

        print("Total: R${:.2f}".format(total))
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


