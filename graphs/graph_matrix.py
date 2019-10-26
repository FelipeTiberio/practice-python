class Vertice():
    def __init__(self, id, cor):
        self.id = id
        self.cor = cor



class Grafo:
    def __init__(self, numVertice) :
        self.numVertice = numVertice 
        self.adjMatrix = []
        self.vertices = []

        # Preenchendo a matrix de adjacencia 
        for i in range(numVertice):
            linha = []
            for j in range(numVertice):
                linha.append(0)
            self.adjMatrix.append(linha)

        # Criando todos os vertices do grafo
        id = 0
        for i in range(numVertice):
            self.vertices.append(id, None)
            id += 1

    def showMatrix(self):
        for i in self.adjMatrix:
            for j in i:
                print(j , end= " ")
            print(" ")

    def addAresta(self, id_vertice1, id_vertice2, rotulo):
        #@TODO Corrijá o código da que para baixo 
        if self.adjMatrix[linha][coluna] ==  1:
            self.vertices[linha][coluna] = Vertice(rotulo)
            return False

        self.adjMatrix[linha][coluna] = 1
        return True

    def removeAresta(self, linha, coluna):

        if self.adjMatrix[linha][coluna] == 0:
            return False
        self.adjMatrix[linha][coluna] = 0
        self.vertices[linha][coluna] = None
        return True

    def existeAresta(self, linha, coluna):
        if self.adjMatrix[linha][coluna] > 0:
            return True
        else:
            return False

    def grauVertice(self, vertice):
        pass

g = Grafo(4)


#g.addAresta(0, 1)

g.showMatrix()
