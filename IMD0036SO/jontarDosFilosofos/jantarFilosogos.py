
from threading import Thread, Lock
from random import randint
import time, os

TEMPOMAXIMO_ESPERA = 10

def esperarFinalizar():
    input_data = None

    while True:
        input_data = input()
        if input_data != None:
            break
    os._exit(0)

class Filosofo (Thread):
    def __init__(self, mesa, fil_id):
        super(Filosofo,self).__init__()
        self.mesa = mesa
        self.philosopher_id = fil_id
        self._is_running = True

    def run (self):
        
        while self._is_running :
            time_wait = randint(0, TEMPOMAXIMO_ESPERA)
            self.think(time_wait)
            self.forks()
            time_wait = randint(0, TEMPOMAXIMO_ESPERA)
            self.eat(time_wait)
            self.leaveForks()

    def think(self,time_wait):
        print("Filosofo", self.philosopher_id + 1 , "está PENSNADO... " )
        time.sleep(randint(0, time_wait))

    def eat(self,time_wait):
        print('Filosofo', self.philosopher_id + 1,"está COMENDO...")
        time.sleep(randint(0, time_wait))

    def forks(self):
        self.mesa.getForks(self.philosopher_id)

    def leaveForks(self):
        self.mesa.leaveForks(self.philosopher_id)

class Mesa():
    def __init__(self):
        self.garfos = [Lock(),Lock(),Lock(),Lock(),Lock()]
    
    def getForks(self, philosopher_id):
        left = philosopher_id
        right = (philosopher_id + 1 ) % 5
        print("Filosofo", philosopher_id + 1 , "está PEGANDO OS GARFOS..")
        self.garfos[left].acquire()
        self.garfos[right].acquire() 

    def leaveForks(self, philosopher_id):
        left = philosopher_id
        right = (philosopher_id + 1 ) % 5
        print("Filosofo", philosopher_id + 1 , "está LIBERANDO OS GARFOS..")
        self.garfos[left].release()
        self.garfos[right].release() 

if __name__ == '__main__':    
    
    print( " ** \t\tJantar dos filosofos\t\t **")
    print("\n \t QUAL QUER INPUT IRÁ FINALIZAR O PROGRAMA \n")
    mesa = Mesa()
    filosofos = []

    for i in range(5):
        filosofos.append(Filosofo(mesa, i) )

    for i in range(5):
        filosofos[i].start()

    Thread( target = esperarFinalizar).start()




        

    

        
    

