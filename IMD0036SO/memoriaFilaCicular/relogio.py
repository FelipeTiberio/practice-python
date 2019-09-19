import time

def conta10():
    time.sleep(10)
    return True
            
class Node():
    def __init__(self, tempo, bitR = 1):
        self.next = None 
        self.bitR  = bitR
        self.tempo = tempo

class Gerenciado():
    def __init__(self):
        self.relogio = Relogio()

    def addProcesso(self, processo):
         for i in range(0,10):
            if self.relogio.nodes[i].bitR_tempo[1] == None:
                self.relogio.addProcesso(i, processo)
            else:
                id = self.removerUltimo()
                self.relogio.addProcesso(i, processo)

    def removerUltimo(self):
        terminou = False

        while not terminou:
            id = self.relogio.self.ultimaPagina % 10 
            if self.relogio.nodes[id].bitR_tempo[0] == 0:
                self.relogio.removerProcesso(id)
            else:
                self.relogio.nodes[id].bitR_tempo[0] =  0
        return True
       
class Relogio():
    def __init__(self):
        self.pages = []
        self._poiter_lastpage = None
        
    def addPage(self,tempo):

        if len(self.pages) >= 10:
            self._swapPage(tempo)
            return

        self.pages.append(Node(tempo))

        if self._poiter_lastpage is None:
            print("Colocando o primerio", tempo) #@DEBUG
            self.pages[0].next = self.pages[0]
            self._poiter_lastpage = 0

        else:
            id_old_lastposition  = len(self.pages) - 2
            id_new_lastposition  = len(self.pages) - 1
            print("Não está mais vázio", tempo)  #@DEBUG
            self.pages[ id_old_lastposition ].next = self.pages[ id_new_lastposition  ]
            self.pages[ id_new_lastposition  ].next = self.pages[0]
    
    def _swapPage(tempo):
        pass

if __name__ == '__main__':

    relogio = Relogio()     
    relogio.addPage(10)
    relogio.addPage(20)
    relogio.addPage(30)

    for node in relogio.pages :
        print(node.tempo,"->", node.next.tempo)


