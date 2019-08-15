from datetime import datetime   # Necessario para pegar a hora do sistema 
from threading import Thread
from random import randint
import time

TEMPOMAXIMO_ESPERA = 5

class Filosofo (Thread):
    def __init__(self, mesa, fil_id):
        super(Filosofo).__init__()
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
        time.sleep(randint(0, time_wait))

    def eat(self,time_wait):
        time.sleep(randint(0, time_wait))

    def forks(self):
        self.mesa.getForks(self.philosopher_id)

    def leaveForks(self, ):
        self.mesa.leaveForks(self.philosopher_id)

    

        
    

