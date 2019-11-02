import math

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
            return False

        if ( id_vertice1 < 0 or id_vertice2 < 0 or id_vertice1 >= self.__numVertice or id_vertice2 >= self.__numVertice):
            print("Valores de vértices não existem.")
            return False

        self.__adjMatrix[id_vertice1][id_vertice2] = 1
        self.__adjMatrix[id_vertice2][id_vertice1] = 1
        
        return True

    def showMatrix(self):
        """ Imprime na tela o estado da matriz de adjacencia @DEBUG """
        GREEN = "\033[0;32m"
        RESET = "\033[0;0m"
        x = 0
        # label coluna
        print(GREEN, end='  ' )
        for i in self.__adjMatrix:
            print("{:3}".format(x) , end = "")
            x+=1
        print(RESET)
        linhalabel = 0
        for i in self.__adjMatrix:
            print(GREEN + "{:2}".format(str(linhalabel)) + RESET, end='')
            #print("{g:}{l:3}{R:}".format(g=GREEN, l= str(linhalabel) , R= RESET, end=""))
            linhalabel +=1
            for j in i:
                print("{:3}".format(j) , end= "")
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

    def __getitem__(self, k):
        """ Sobrecarrega o operado a[k] para retorna o k-esimo vértice """ 
        return self.vertices[k]

    def __len__(self):
        return self.__numVertice

    def adjSudoku(self):
        quant_lateral = int(math.sqrt(self.__numVertice))
        numlinha = 0
        
        pass
    
    
           




def main():    

    g = Grafo(16)

    g.addAresta(0, 1)
    g.removeAresta(1,0)

    g.adjSudoku()

    g.showMatrix()

    

    

if (__name__ == '__main__'):
    main()