
from threading import Thread, Condition, enumerate
from random import randint
import time

GREEN = "\033[0;32m"
RESET = "\033[0;0m"
Quantum = 5 # Tempo que cada processo tera no processador para terminar sua tarefa antes de ir para o fim da fila   

'''Cada um das thread tenham um tempo de processamento randomico entre MIN e MAX '''
MIN = 5  
MAX = 15
                
MAXTHREADS = 7 # O numero maximo de threads eh entre 3 e MAXTHREADS

MAXVALORPRIORIDADE = 5 # IREI gerar os valores de prioridade de forma randomica de 0 a MAXVALORPRIORIDADE

filasDePrioridade = {} # {valor_prioridade : fila com o valor_prioridade} 

id_thread = 1 # apenas uma variavez para usar como id de thread

def cpu( thread_da_vez  ):
    """Executa uma thread ate que ela finalize seu processo \n
       a thread pode nao ter sido iniciada ainda, ou esta esperando """

    if not thread_da_vez.isAlive():
        thread_da_vez.start()

    elif ( thread_da_vez and not thread_da_vez.can_woke ):
        thread_da_vez.continuar_processo()

def round_robin( fila ):
    
    while len(fila) > 0  :

         thread_da_vez = fila.pop(0)
         if thread_da_vez.terminei or thread_da_vez.falta == 0: # linha onde removo as threads que acabaram da fila
             continue
         cpu(thread_da_vez)
         time.sleep(Quantum)
         thread_da_vez.esperar()
         fila.append(thread_da_vez)

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
        self.can_woke = False
        if self.falta != 0:
            print("\t-Sou a thread nº ", self.id , " meu tempo de quantum acabou, irei para o fim da fila... ")
        
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
    print(GREEN + "| Quantidade de Threads: ", quantidade_t  , " Tempo de quantum de cpu :", Quantum, "segundos |") #TODO tenho de fazer um novo
    print("\tQuantidade de processos em cada uma das filas:")
    n = 0
    for chave in filasDePrioridade:
        print("\t **Prioridade", n, " são:", len(filasDePrioridade[chave]))
        n += 1
    print(RESET)

def polular_fila():
    """ popula a fila com com todas as suas listas de prioridades, bem como, todas as threads s"""
    numero_de_threads = randint(3, MAXTHREADS)
    global id_thread

    for valor_prioridade in range(0, MAXVALORPRIORIDADE):   # Chaves para o dicionario
        if valor_prioridade not in filasDePrioridade:
            filasDePrioridade[valor_prioridade] = []
    
    for i in range(0,numero_de_threads):                    # Colocando cada thread na fila correta 

        tempo_processamento = randint(MIN, MAX)
        prioridade          = randint(0,MAXVALORPRIORIDADE-1)
        nova_thread         = MinhaThread(id_thread, tempo_processamento, prioridade)
        filasDePrioridade[prioridade].append(nova_thread)
        id_thread           +=1

def porPrioridades():
    """Processa a fila de prioridade nao vazia de prioridade mais alta  """
    i = 0
    for chave in filasDePrioridade:   # Iterando as filas.
        if(len(filasDePrioridade[chave]) == 0):               # Se A fila eh vazia, ir para a proxima.
            i+=1
            continue 
        print(GREEN + "\t ** Iniando a fila de prioridade: ", i, "**"+  RESET ) 
        round_robin(filasDePrioridade[chave])
        return

def aumentarPrioridadeDeFila(): 
    IdFilasAumentaPrioridade = [] # id para evitar stavation
    
    for chave in filasDePrioridade:
        if( len(filasDePrioridade[chave]) != 0 and chave != 0 ):
            IdFilasAumentaPrioridade.append(chave)

    print(GREEN + "\n** Aumento em uma unidade os processos de prioridade : ", end="")
    for aux in IdFilasAumentaPrioridade:
        print(aux," ", end='')
    print(" para evitar STARVATION." + RESET)

    for i in IdFilasAumentaPrioridade:
        fila_para_aumentar = filasDePrioridade[i]
        filasDePrioridade[i -1] = fila_para_aumentar
        filasDePrioridade[i].clear()

def filasEstaoVazias():
    """ retorna verdadeiro quando todas as filas de prioridade estao vazia, retorna falso caso contrario"""
    n = 0
    for chave in filasDePrioridade:
        n += len(filasDePrioridade[chave])

    if n == 0:
        return True
    return False

if __name__ == '__main__': 

    terminou = False

    polular_fila()
    configuracao_inicial()

    ''' iniciado as filas de prioridade  '''
    porPrioridades()
    porPrioridades()

    ''' Criando mais 3 threads '''
    MAXTHREADS = 3 
    aumentarPrioridadeDeFila()
    polular_fila()
    print()
    configuracao_inicial()
    print()
    
    while True:
        porPrioridades()

        if filasEstaoVazias():
            break

    print( GREEN + "** Estado final de todas as filas **")
    print(filasDePrioridade)