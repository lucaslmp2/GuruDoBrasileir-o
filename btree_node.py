class Node:
    def __init__(self, order):
        self.keys = []  # Inicializa uma lista vazia para armazenar as chaves no nó
        self.values = []  # Inicializa uma lista vazia para armazenar os valores correspondentes às chaves
        self.children = []  # Inicializa uma lista vazia para armazenar os filhos do nó
        self.order = order  # Define a ordem da árvore B (o número máximo de chaves permitido em um nó)

    def insert(self, key, value):
        # Encontre a posição de inserção no nó folha
        index = 0  # Inicializa um índice para rastrear a posição de inserção
        while index < len(self.keys) and key > self.keys[index]:
            index += 1  # Avança no índice enquanto a chave a ser inserida é maior que a chave atual

        # Insira a chave e o valor na posição adequada
        self.keys.insert(index, key)  # Insere a chave na posição apropriada na lista de chaves
        self.values.insert(index, value)  # Insere o valor correspondente à chave na lista de valores

        # Verifique se o nó folha está cheio
        if len(self.keys) > self.order:
            # Divida o nó folha
            self.split()  # Chama o método de divisão se o nó folha estiver cheio

    def split(self):
        # Divida o nó folha em dois
        middle = len(self.keys) // 2  # Calcula o ponto médio das chaves
        new_node = Node(self.order)  # Cria um novo nó

        new_node.keys = self.keys[middle:]  # As chaves da direita do ponto médio vão para o novo nó
        new_node.values = self.values[middle:]  # Os valores correspondentes também são movidos
        new_node.children = self.children  # Os filhos não são divididos, então ambos compartilham a mesma lista

        self.keys = self.keys[:middle]  # Atualiza as chaves do nó atual para incluir apenas as chaves da esquerda
        self.values = self.values[:middle]  # Atualiza os valores correspondentes
        self.children = [new_node]  # Atualiza os filhos para conter o novo nó à direita

    def search(self, key):
        # Encontre o índice apropriado para continuar a pesquisa
        index = 0  # Inicializa um índice para rastrear a posição da chave
        while index < len(self.keys) and key > self.keys[index]:
            index += 1  # Avança no índice enquanto a chave de pesquisa é maior que a chave atual

        # Verifica se a chave foi encontrada neste nó
        if key == self.keys[index]:
            return self.values[index]  # Retorna o valor correspondente à chave se for encontrada

        # Se não foi encontrado aqui, continue a pesquisa nos filhos
        return self.children[index].search(key)  # Chama a pesquisa no filho apropriado

class BTree:
    def __init__(self, order):
        self.root = None  # Inicializa a raiz da árvore como nula (vazia)
        self.order = order  # Define a ordem da árvore B (o número máximo de chaves permitido em um nó)

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(self.order)  # Se a raiz for nula, crie um novo nó folha como raiz
        self.root.insert(key, value)  # Chama o método de inserção no nó raiz

    def search(self, key):
        if self.root is not None:
            return self.root.search(key)  # Chama o método de pesquisa no nó raiz, se a raiz não for nula
        else:
            return None  # Retorna None se a árvore estiver vazia (raiz é nula)
