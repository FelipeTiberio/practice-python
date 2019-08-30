from threading import Thread, Lock, Condition
from random import randint
import time, os

Quantum = 5 

def cpu( thread_da_vez  ):
    thread_da_vez.start()

class MinhaThread( Thread ):
    def __init__(self, simbolo, id, tempo):
        super(MinhaThread, self).__init__()
        self.simblo = simbolo
        self.id = id
        self.can_woke = True
        self.condition = Condition()
        self.tempo = tempo
    
    def run(self):
        with self.condition:
            for i in range(self.tempo):
                if not self.can_woke:
                    self.condition.wait()  
                print("simbolo")
                time.sleep(1)

    def esperar(self):
        self.can_woke =False
        print("@debug esperando 3 segudos ")
        
    def continuar_processo(self):
        with self.condition:
            self.condition.notify()
            self.can_woke = True


# teste 
t = MinhaThread('|||', 1, 10)
t.start()
t.esperar()
time.sleep(3)
t.continuar_processo()




