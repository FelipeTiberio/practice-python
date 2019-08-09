import os
import time
import subprocess 

pids = []

# finaliza o processo de pid==pid
def finalizarProcesso(pid):
  oldlen = len(pids)
  existe_pid = True

  if int(pid) not in pids:
    print( "\n *** VALOR DE FILHO NÃO É UM PROCESSO FILHO. *** \n")
    return False

  if os.getpid() != 0:
    os.waitpid(int(pid),0)
    subprocess.call(['sleep','1'])
    pids.remove(int(pid))

  if oldlen != len(pids):
    print( " \n ---- Processo de "+ pid + " finalizado. --- \n")

  return True

  

def listra_processos_python():
  if os.getpid() != 0:
    subprocess.call( ['ps', '-C', 'python3'])
    print()
    
# Inicialziando os processos.
def inicializar_4_processo():
  for i in range(4):
      if os.getpid() != 0:
        newpid = os.fork()
      if newpid != 0:
          print( str(i+1) + "º processo com pid", newpid, "criado. ")
          pids.append( newpid )
      else:
        os._exit(0)

def menu():
  print( "\n Escreva o pid do processo que gostaria de finalizar ")
 

if __name__ == '__main__':
  inicializar_4_processo()

  while len(pids) != 0:
    menu() 
    listra_processos_python() 
    pid = input()

    finalizarProcesso(pid)


