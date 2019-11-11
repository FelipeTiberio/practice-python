[1mdiff --git a/graphs/graph_matrix.py b/graphs/graph_matrix.py[m
[1mindex b4190db..819a64c 100644[m
[1m--- a/graphs/graph_matrix.py[m
[1m+++ b/graphs/graph_matrix.py[m
[36m@@ -2,7 +2,7 @@[m [mimport math[m
 [m
 class Vertice():[m
     def __init__(self, tupla, cor = None):[m
[31m-        """Atributo tupla (i,j) equivale a linha i e coluna j do jogo de Sudoku .\n[m
[32m+[m[32m        """ Atributo tupla (i,j) equivale a linha i e coluna j do jogo de Sudoku .\n[m
         Atribito cor é o inteiro que marca o número preenchido no jogo."""[m
         self.tupla = tupla[m
         self.cor = cor[m
[36m@@ -128,6 +128,7 @@[m [mclass Grafo:[m
     def __len__(self):[m
         return self.__numVertice[m
 [m
[32m+[m
     def adjSudoku(self):[m
         """ Dois vértices (i,j) e (i´,j´) são adjacentes quando i=i´ ou j=j´ """[m
         [m
[36m@@ -146,8 +147,16 @@[m [mclass Grafo:[m
                 incide2 = self.vertices.index(v2)[m
                 self.addAresta(incide2,incide1)[m
 [m
[31m-            for v2 in self.vertices: # adjacendi em blocos @TODO está errada [m
[31m-                if ((v1.tupla[0]/self.__n) ==(v2.tupla[0]/self.__n) and (v1.tupla[1]/self.__n) == (v2.tupla[1]/self.__n) ):[m
[32m+[m[41m            [m
[32m+[m[32m            for v2 in self.vertices: # adjacencia entre os quadrantes @TODO (Ainda está errado )[m
[32m+[m[32m                v1_quadrante_linha  = ( v1.tupla[0] % int(math.sqrt(self.__numVertice)) ) / self.__n[m
[32m+[m[32m                v1_quadrante_coluna = ( v1.tupla[1] / int(math.sqrt(self.__numVertice)) ) / self.__n[m
[32m+[m[32m                v2_quadrante_linha  = ( v2.tupla[0] % int(math.sqrt(self.__numVertice)) ) / self.__n[m
[32m+[m[32m                v2_quadrante_coluna = ( v2.tupla[1] / int(math.sqrt(self.__numVertice)) ) / self.__n[m[41m [m
[32m+[m
[32m+[m[32m               # print( "v1_quadrante_linha =  {v1l:3} | e v2_quandante_colonua = {v2c:}".format( v1l = v1_quadrante_linha, v2c = v2_quadrante_coluna) )[m
[32m+[m[32m                #print( "v1_quadrante_coluna = {v1l:3} | e v2_quandante_linha = {v2c:}".format( v1l = v1_quadrante_coluna, v2c = v2_quadrante_linha) )[m
[32m+[m[32m                if ( (v1_quadrante_linha == v2_quadrante_linha) and ( v2_quadrante_coluna == v1_quadrante_coluna  ) ):[m
                     incide1 = self.vertices.index(v1)[m
                     incide2 = self.vertices.index(v2)[m
                     self.addAresta(incide2,incide1)[m
[36m@@ -159,7 +168,7 @@[m [mdef printSudoku(vertices):[m
     count = 1[m
 [m
     for v in vertices:[m
[31m-        [m
[32m+[m
         if(v.cor == None):[m
             print("{ponto:3}".format( ponto="."), end= "")[m
         else:[m
[36m@@ -168,7 +177,8 @@[m [mdef printSudoku(vertices):[m
         if( (count % n) == 0 ):[m
             print()[m
         count += 1[m
[31m-[m
[32m+[m[41m        [m
[32m+[m[41m        [m
 [m
 [m
 def main():    [m
[36m@@ -177,9 +187,9 @@[m [mdef main():[m
     [m
     g.adjSudoku()[m
     [m
[31m-    g. showMatrixWithTuples()[m
[32m+[m[32m    g.showMatrixWithTuples()[m
 [m
[31m-    printSudoku(g.vertices)[m
[32m+[m[32m    #printSudoku(g.vertices)[m
    [m
 [m
 [m
