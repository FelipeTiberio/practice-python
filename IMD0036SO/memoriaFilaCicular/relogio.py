import time


def conta10():
    time.sleep(10)
    return True
            
class Node():
    def __init__(self, id):
        self.id  = id 
        self.next = None 
        self.bitR_tempo = (0, None) 

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
        self.nodes = []
        self.ultimaPagina = 0
        self.counter = 0

        for i in range(0,10):
            self.nodes.append(  Node(i) )

        for i in range(0,9):
            self.nodes[i].next = self.nodes[i+1]
        
        self.nodes[9].next = self.nodes[0]
        
    def addpagina(self, id ,tupla):
        self.counter +=1
        self.ultimaPagina += 1
        self.ultimaPagina = self.ultimaPagina % 10
        self.nodes[id] = tupla

    def removerProcesso(self, id):
        self.counter -= 1

        if self.counter != 0:
            self.relogio.nodes[id] = (0, None)


relogio = Relogio()     

for n in  relogio.nodes :
    print(n.next.id)

gerenciado =  Gerenciado()
gerenciado.addProcesso(1)
