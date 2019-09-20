import time
from threading import Thread
from multiprocessing.pool import ThreadPool

MAXLENLINE = 3
TIMESLEEP = 10

def conta10segundos(page):
    time.sleep(TIMESLEEP)
    page.bitR = 0
    return True
            
class Node():
    def __init__(self, tempo, bitR = 1):
        self.next = None 
        self.bitR  = bitR
        self.tempo = tempo

    def whaitAndChangeBit(self):
        x = Thread(target=conta10segundos, args=(self,))
        x.start()
            
class GerenciadorMemoria():
    def __init__(self):
        self.relogio = Relogio()

    def addProcesso(self, tempo):
        self.relogio.addPage(tempo)

    def listarPaginas(self):
        pages = self.relogio.pages
        print("\t** Páginas na lista **")

        for i in range(0, len(pages)):
            print("[Pagina id: {id:}| bitR : {bit:} | tempo : {tempo:}]".format( id= i, bit =pages[i].bitR, tempo = pages[i].tempo ))

    def menu(self):
        op = -1

        while op != 0:
            print("-----")
            print("Digite 1 para criar uma nova página.")
            print("Digite 2 para listar as páginas que estão na fila.")
            print("Digite 3 para finalizar o programa")
            op = input()

            if op == '1':
                self.addProcesso(10)
            if op == '2':
                self.listarPaginas()
            if op == '3':
               pass
       
class Relogio():
    def __init__(self):
        self.pages = []
        self._poiter_lastpage = None
        
    def addPage(self,tempo):

        if len(self.pages) >= MAXLENLINE : #Fila está cheia
            self._swapPage(tempo)
            return

        newPage = Node(tempo)           # Nava Página
        self.pages.append(newPage)      # colocando a nova pagina na fila
        newPage.whaitAndChangeBit()     # iniciando o cantado de 10 segundos da página 

        if self._poiter_lastpage is None:
            self.pages[0].next = self.pages[0]
            self._poiter_lastpage = 0

        else:
            id_old_lastposition  = len(self.pages) - 2
            id_new_lastposition  = len(self.pages) - 1
            self.pages[ id_old_lastposition ].next = self.pages[ id_new_lastposition  ]
            self.pages[ id_new_lastposition  ].next = self.pages[0]
    
    def _swapPage(self, tempo):
        swapped = False
        pages = self.pages

        while not swapped:
            if pages[self._poiter_lastpage].bitR == 0:
                self._removePage(self._poiter_lastpage) # Removendo a pagina antiga
                self._addNewPageToPositon(self._poiter_lastpage, tempo) # colocando a página nova
                swapped = True
            else:
                self.pages[self._poiter_lastpage].bitR = 0
                self._poiter_lastpage = (self._poiter_lastpage + 1) % len(self.pages) 

    def _removePage(self, position):
        nextIdPage = ( position + 1) % len(self.pages)
        previousIdPage = (position - 1 ) % len(self.pages)

        self.pages[previousIdPage].next = self.pages[nextIdPage]
        self.pages.pop(position)
    
    def _addNewPageToPositon(self, position, tempo):
        nextIdPage = ( position + 1) % len(self.pages)
        previousIdPage = (position - 1 ) % len(self.pages)

        newPage = Node(tempo)
        newPage.whaitAndChangeBit()

        newPage.next = self.pages[previousIdPage].next

        self.pages[previousIdPage].next = newPage
        self.pages.insert(position, newPage)
            


        


if __name__ == '__main__':

    gerenciado = GerenciadorMemoria()

    gerenciado.menu()


