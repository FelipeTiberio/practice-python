import time
from threading import Thread

MAXLENLINE = 3
TIMESLEEP = 10

def conta10segundos():
    time.sleep(TIMESLEEP)
    return True
            
class Node():
    def __init__(self, tempo, bitR = 1):
        self.next = None 
        self.bitR  = bitR
        self.tempo = tempo

    def whaitAndChangeBit():
        while True:
            Thread(conta10segundos).start

class Gerenciado():
    def __init__(self):
        self.relogio = Relogio()

    def addProcesso(self, tempo):
        self.relogio.addPage(tempo)

       
class Relogio():
    def __init__(self):
        self.pages = []
        self._poiter_lastpage = None
        
    def addPage(self,tempo):

        if len(self.pages) >= MAXLENLINE : #Fila está cheia
            self._swapPage(tempo)
            return

        self.pages.append(Node(tempo))

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

        newPage.next = self.pages[previousIdPage].next

        self.pages[previousIdPage].next = newPage
        self.pages.insert(position, newPage)
            


        


if __name__ == '__main__':

    relogio = Relogio()     
    relogio.addPage(10)
    relogio.addPage(20)
    relogio.addPage(30)
    relogio.addPage(40)
    
    for node in relogio.pages :
        print(node.tempo,"->", node.next.tempo)


