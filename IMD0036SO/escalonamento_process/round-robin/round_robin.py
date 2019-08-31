from threading import Thread, Lock, Condition, enumerate
from random import randint
import time, os

Quantum       = 5 # Tempo que cada processo tera no processador para terminar sua tarefa antes de ir para o fim da fila   

#'''Eu fiz com que cada um das thread tenham um tempo de processamento randomico entre MIN e MAX '''
MIN           = 5  
MAX           = 15
                
MAXTHREADS    = 5 # O número maximo de threads eh entre 3 e MAXTHREADS

filaDeThreads = [] 

def cpu( thread_da_vez  ):
    """Executa uma thread ate que ela finalize seu processo \n
       a thread pode nao ter sido iniciada ainda, ou esta esperando """

    if not thread_da_vez.isAlive():
        thread_da_vez.start()

    elif ( thread_da_vez and not thread_da_vez.can_woke ):
        thread_da_vez.continuar_processo()

class MinhaThread( Thread ):

    def __init__(self, id, tempo):
        super(MinhaThread, self).__init__()
        self.id = id
        self.can_woke = True
        self.condition = Condition()
        self.tempo = tempo
        self.falta = tempo
        self.terminei = False
    
    def run(self):
        with self.condition:
            for i in range(self.tempo):
                if not self.can_woke:
                    self.condition.wait()  
                print("* Processando thread nº", self.id  , "falta", self.falta, " para acabar meus procesos xD.")
                time.sleep(1)
                self.falta = self.falta -1 
            print(" \t-Terminei de processar, sou a thread ", self.id, ".")
            self.terminei = True

    def esperar(self):
        self.can_woke =False
        if self.falta > 0:
            print("\t-Sou a thread ", self.id , " meu tempo de quantum acabou, irei para o fim da fila... ")
        
    def continuar_processo(self):
        with self.condition:
            self.condition.notify()
            self.can_woke = True

def round_robin():
    """ processa uma thread ate que ela nao tenha mais dados para serem carregas \n
        ou o tempo de Quantum acabar, então a thread que estava em proecesso ira para o fim da fila  """
    while len(filaDeThreads) > 0  :

         thread_da_vez = filaDeThreads.pop(0)
         if thread_da_vez.terminei or thread_da_vez.falta == 0: # linha onde removo as threads que acabaram da fila
             continue
         cpu(thread_da_vez)
         time.sleep(Quantum)
         thread_da_vez.esperar()
         filaDeThreads.append(thread_da_vez)

def configuracao_inicial():
    print("| Quantidade de Threads: ", len(filaDeThreads) , " Tempo de quantum de cpu :", Quantum, "segundos |\n")

def polular_fila():
    numero_de_threads = randint(3, MAXTHREADS)
    id_thread = 1

    for i in range(0,numero_de_threads):
        tempo_processamento = randint(MIN, MAX)
        filaDeThreads.append( MinhaThread(id=id_thread, tempo=tempo_processamento))
        id_thread +=1

if __name__ == '__main__':   

    polular_fila()
    configuracao_inicial()
    round_robin()



