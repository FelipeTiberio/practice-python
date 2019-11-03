import math

class Vertice():
    def __init__(self, tupla, cor = None):
        """Atributo tupla (i,j) equivale a linha i e coluna j do jogo de Sudoku .\n
        Atribito cor é o inteiro que marca o número preenchido no jogo."""
        self.tupla = tupla
        self.cor = cor
       
    def __eq__(self, x):
        if self.tupla == x.tupla:
            return True
        else:
            return False

class Grafo:
    def __init__(self, tamanho_bloco) :
        """ O argumento tamanho do bloco representa o tamanho do lado das regiões do sudoku.
            Para criar uma instancia de um sudoko do tipo 9x9 o tamanho do bloco será de 3.
            Para criar uma instancia de um sudoko do tipo 4x4 o tamanho do bloco será de 2. """

        self.__numVertice = pow(tamanho_bloco,2) * pow(tamanho_bloco,2)
        self.__adjMatrix = []
        self.vertices = []
        self.__n = int(math.sqrt(self.__numVertice))
        
        for i in range(self.__numVertice): # Preenchendo a matrix de adjacencia 
            linha = []
            for j in range(self.__numVertice):
                linha.append(0)
            self.__adjMatrix.append(linha)
       
        for i in range( 1 , self.__n + 1 ): # Criando todos os vertices do grafo, estou usando tuplas (i,j) para representar a linha e coluna de cada vértice
            for j in range(1 , self.__n + 1):
                self.vertices.append( Vertice( ( int(i % (self.__n + 1)) ,j),None ) )



    def addAresta(self, id_vertice1, id_vertice2):
        """ Rebece os indices, no vetor de vertices, e os torna adjacentes atualizado a matrix de adjacência. """
        if ( id_vertice1 == id_vertice2  ):
            return False

        if ( id_vertice1 < 0 or id_vertice2 < 0 or id_vertice1 >= self.__numVertice or id_vertice2 >= self.__numVertice):
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

    def showMatrixWithTuples(self):
        """ Imprime na tela o estado da matriz de adjacencia com label de tuplas @DEBUG """
        GREEN = "\033[0;32m"
        RESET = "\033[0;0m"
        
        # label coluna
        print(GREEN, end='       ' )
        for i in self.vertices:
            print("{:} ".format(str(i.tupla)) , end = "")
           
        print(RESET)
        linhalabel = 0
        for i in self.__adjMatrix:
            print(GREEN + "{:2}".format(str(self.vertices[linhalabel].tupla )) + RESET, end='')
            #print("{g:}{l:3}{R:}".format(g=GREEN, l= str(linhalabel) , R= RESET, end=""))
            linhalabel +=1
            for j in i:
                print("{:3}".format(j) , end= "    ")
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
        return self.vertices[k]

    def __len__(self):
        return self.__numVertice

    def adjSudoku(self):
        """ Dois vértices (i,j) e (i´,j´) são adjacentes quando i=i´ ou j=j´ """
        
        for v1 in self.vertices:
            for linha in range(1 , self.__n + 1): # adjacencia em colunas
                v2 = Vertice( (linha, v1.tupla[1]), None ) 

                incide1 = self.vertices.index(v1)
                incide2 = self.vertices.index(v2)
                self.addAresta(incide2,incide1)

            for coluna in range(1 , self.__n + 1): # adjacencia em linhas
                v2 = Vertice( (v1.tupla[0],coluna ), None ) 
                
                incide1 = self.vertices.index(v1)
                incide2 = self.vertices.index(v2)
                self.addAresta(incide2,incide1)

            for v2 in self.vertices: # adjacendi em blocos @TODO está errada 
                if ((v1.tupla[0]/self.__n) ==(v2.tupla[0]/self.__n) and (v1.tupla[1]/self.__n) == (v2.tupla[1]/self.__n) ):
                    incide1 = self.vertices.index(v1)
                    incide2 = self.vertices.index(v2)
                    self.addAresta(incide2,incide1)


def printSudoku(vertices):
    """ Recebe os vértices que representão o sudoko e imprime na tela o estado atual do jogo """ 
    n = int( math.sqrt(len(vertices)) )
    count = 1

    for v in vertices:
        
        if(v.cor == None):
            print("{ponto:3}".format( ponto="."), end= "")
        else:
            print("{cor:3}".format(cor=str(v.cor)), end = "" )

        if( (count % n) == 0 ):
            print()
        count += 1



def main():    

    g = Grafo(2)
    
    g.adjSudoku()
    
    g. showMatrixWithTuples()

    printSudoku(g.vertices)
   


if (__name__ == '__main__'):
    main()