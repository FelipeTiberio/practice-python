from threading import Thread, Lock, Condition, enumerate
from random import randint
import time, os

Quantum = 5 

filaDeThreads = []
def cpu( thread_da_vez  ):
    """Executa uma thread ate que ela finalize seu processo \n
       essa pode não ter sido iniciada ainda, ou esta esperando """

    if not thread_da_vez.isAlive():
        thread_da_vez.start()

    elif ( thread_da_vez and not thread_da_vez.can_woke ):
        thread_da_vez.continuar_processo()

class MinhaThread( Thread ):
    def __init__(self, simbolo, id, tempo):
        super(MinhaThread, self).__init__()
        self.simblo = simbolo
        self.id = id
        self.can_woke = True
        self.condition = Condition()
        self.tempo = tempo
        self.falta = tempo
        self.terminoi = False
    
    def run(self):
        with self.condition:
            for i in range(self.tempo):
                if not self.can_woke:
                    self.condition.wait()  
                print(" processando thread nº", self.id , " ", self.simblo , "falta", self.falta)
                time.sleep(1)
                self.falta = self.falta -1 
            print("Salut, terminei de processar, sou a thread ", self.id)
            self.terminoi = True

    def esperar(self):
        self.can_woke =False
        print("Sou a thread ", self.id , " vou para o fim da fila... ")
        
    def continuar_processo(self):
        with self.condition:
            self.condition.notify()
            self.can_woke = True

def round_robin():
    
    while len(filaDeThreads) > 0  :

         thread_da_vez = filaDeThreads.pop(0)
         if thread_da_vez.terminoi :
             continue

         cpu(thread_da_vez)
         time.sleep(Quantum)
         thread_da_vez.esperar()
         filaDeThreads.append(thread_da_vez)

# teste 
filaDeThreads.append( MinhaThread("|||",1,10))
filaDeThreads.append( MinhaThread("|||",2,8))

'''
t = MinhaThread('|||', 1, 10)
cpu(t)
t.esperar()
time.sleep(3)
cpu(t)
#t.continuar_processo()
'''

round_robin()



