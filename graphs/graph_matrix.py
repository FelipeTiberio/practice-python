class Vertice():
    def __init__(self, id, cor):
        self.id = id
        self.cor = cor


class Grafo:
    def __init__(self, numVertice) :
        self.__numVertice = numVertice 
        self.__adjMatrix = []
        self.vertices = []

        # Preenchendo a matrix de adjacencia 
        for i in range(numVertice):
            linha = []
            for j in range(numVertice):
                linha.append(0)
            self.__adjMatrix.append(linha)

        # Criando todos os vertices do grafo
        id = 0
        for i in range(numVertice):
            self.vertices.append( Vertice(id, None))
            id += 1

    def addAresta(self, id_vertice1, id_vertice2):
        if ( id_vertice1 == id_vertice2  ):
            print("A vérteces são iguais.")
            return

        if ( id_vertice1 < 0 or id_vertice2 < 0 or id_vertice1 >= self.__numVertice or id_vertice2 >= self.__numVertice):
            print("Valores de vértices não existem.")
            return

        self.__adjMatrix[id_vertice1][id_vertice2] = 1
        self.__adjMatrix[id_vertice2][id_vertice1] = 1
        
        return True

    def showMatrix(self):
        for i in self.__adjMatrix:
            for j in i:
                print("{:2}".format(j) , end= " ")
            print(" ")

    def removeAresta(self,  id_vertice1, id_vertice2):

        if ( id_vertice1 == id_vertice2  ):
            print("A vérteces são iguais.")
            return

        if ( id_vertice1 < 0 or id_vertice2 < 0 or id_vertice1 >= self.__numVertice or id_vertice2 >= self.__numVertice):
            print("Valores de vértices não existem.")
            return

        if self.__adjMatrix[ id_vertice1][id_vertice2] == 0:
            return False

        self.__adjMatrix[ id_vertice1][id_vertice2] = 0
        self.__adjMatrix[id_vertice2][ id_vertice1] = 0

        return True

    def existeAresta(self, v1, v2):
        try:
            return True if self.__adjMatrix[v1][v2] > 0 else False

        except IndexError:
            print("Valores:", v1,"e", v2, "não são íncides válidos" )

    def grauVertice(self, vertice):
        pass

    def getMatrixAdj(self):
        return self.__adjMatrix

    def __len__(self):
        return self.__numVertice


g = Grafo(4)

g.addAresta(0, 1)

g.showMatrix()
