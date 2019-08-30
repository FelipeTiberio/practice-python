from threading import Thread, Condition, enumerate
from random import randint
import time

Quantum = 5 # Tempo que cada processo terá no processador para terminar sua tarefa antes de ir para o fim da fila   

#'''Eu fiz com que cada um das thread tenham um tempo de processamento randomico entre MIN e MAX '''
MIN = 5  
MAX = 15
                
MAXTHREADS = 5 # O número maximo de threads eh entre 3 e MAXTHREADS

MAXVALORPRIORIDADE = 5 # IREI gerar os valores de prioridade de forma randomica de 0 a MAXVALORPRIORIDADE

filasDePrioridade = {} # {valor_prioridade : fila com o valor_prioridade} 
 

def cpu( thread_da_vez  ):
    """Executa uma thread ate que ela finalize seu processo \n
       a thread pode não ter sido iniciada ainda, ou esta esperando """

    if not thread_da_vez.isAlive():
        thread_da_vez.start()

    elif ( thread_da_vez and not thread_da_vez.can_woke ):
        thread_da_vez.continuar_processo()

class MinhaThread( Thread ):
    def __init__(self, id, tempo, prioridade = 0 ):
        super(MinhaThread, self).__init__()
        self.id             = id
        self.can_woke       = True
        self.condition      = Condition()
        self.tempo          = tempo
        self.falta          = tempo
        self.terminei       = False
        self.prioridade     = prioridade
        self.tempo_de_fila  = 0
    
    def run(self):
        with self.condition:
            for i in range(self.tempo):
                if not self.can_woke:
                    self.condition.wait()  
                print("* Processando thread nº", self.id  , "falta", self.falta, " para acabar meus procesos xD.")
                time.sleep(1)
                self.falta  = self.falta -1 

            print(" \t-Terminei de processar, sou a thread ", self.id, ".")
            self.terminei   = True

    def esperar(self):
        self.can_woke =False
        if self.falta > 0:
            print("\t-Sou a thread ", self.id , " meu tempo de quantum acabou, irei para o fim da fila... ")
        
    def continuar_processo(self):
        with self.condition:
            self.condition.notify()
            self.can_woke = True

    def aumentarPrioridade(self):
        self.prioridade +=1


def configuracao_inicial():
    quantidade_t = 0
    for i in filasDePrioridade:
        quantidade_t += len(filasDePrioridade[i])
    print("| Quantidade de Threads: ", quantidade_t  , " Tempo de quantum de cpu :", Quantum, "segundos |\n") #TODO tenho de fazer um novo
    #@TODO a quantidade de cada uma das filas

def polular_fila():
    numero_de_threads = randint(3, MAXTHREADS)
    id_thread = 1

    for valor_prioridade in range(0, MAXVALORPRIORIDADE):   # Chaves para o dicionario
        if valor_prioridade not in filasDePrioridade:
            filasDePrioridade[valor_prioridade] = []
    
    for i in range(0,numero_de_threads):                    # Colocando cada thread na fila correta 

        tempo_processamento = randint(MIN, MAX)
        prioridade          = randint(0,MAXVALORPRIORIDADE-1)
        nova_thread         = MinhaThread(id_thread, tempo_processamento, prioridade)
        filasDePrioridade[prioridade].append(nova_thread)
        id_thread           +=1




if __name__ == '__main__':   

    polular_fila()
    configuracao_inicial()
    print(filasDePrioridade)