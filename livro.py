from gerenciador_de_arquivos import GerenciadorDeArquivos
class Livro:
    def __init__(self):
        self.estoque = GerenciadorDeArquivos('estoque/estoque.csv')

    def inserir(self):
        isbn = input('informe o ISBN: ')
        self.estoque.buscar_em_arquivo('isbn', isbn)

        if(isbn in self.estoque):
            quantidade = int(input('Esse livro já está cadastrado no sistema, por favor, informe a quantidade a ser adicionada: '))
            self.estoque.atualizar_livro(isbn, 'quantidade', self.estoque.buscar_em_arquivo('isbn', isbn)['quantidade'] + quantidade)
        else:
            produto = input('Informe o nome do livro: ')
            valor = float(input('Informe o valor do Livro: '))
            quantidade = int(input('Informe a quantidade: '))

            self.estoque.adicionar_linha({'isbn': isbn, 'nome': produto, 'quantidade': quantidade, 'valor': valor})

    def excluir(self):
        produto = input('informe o isbn do produto, essa ação deletará todos os registros: ')
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
