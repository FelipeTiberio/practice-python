import  subprocess, os, time,sys, signal
from threading import Thread
ENTRADACOMAND1= 'ps -aux | grep python3 '

def proc_start():
	if os.getpid() != 0:
		newpid = os.fork()
	
	if newpid == 0:
		time.sleep(10)
		print(" PASSOU 10 SEGUNDOS {d:}".format(d = os.getpid()))
		Thread(target=proc_start).start()
		time.sleep(10)
		print(" PASSOU 20 SEGUNDOS {d:}".format(d = os.getpid()))
		Thread(target=proc_start).start()
		time.sleep(10)
		print(" PASSOU 30 SEGUNDOS {d:}".format(d = os.getpid()))
		Thread(target=proc_start).start()
		print( ".. OS 30 SEGUNDOS DO {proc:} TERMINARAM, ELE IRÀ SER FINALIZADO ..".format( proc = os.getpid()))
		finalizarProcesso(  int(os.getpid()) )
		os._exit(0)

	return

def checkout_comand( args  ):
	""" retorna todos os processo do sisteam em uma lista, cada item da lista é uma linha do comando args   """
	stdout = subprocess.check_output( args , shell=True)
	return stdout.decode().split('\n')

def get_matrix_process( str_lines ):
	""" retorna uma matriz com o texo recebido """
	matrix = []
	maxsplit = (len(str_lines[0].split()))-1 # a quantidade de colunas de matrix sera os rotulos do output de subprocess(ps)
	
	for line in str_lines:					 # criando a matrix com a saida de ps 
		matrix.append( line.split( maxsplit= maxsplit ))
	return matrix

def get_process_mtx_formated( mtx ):
	"""
	Retorna a matrix formatada para imprimir na tela os processos e suas informaçoes 
	"""
	str_formated = []
	for line in mtx:
		for i in range(len(line)):
			str_aux = "{user:12s} {pid:5s} {men:5s} {comand:56s} {pipe:5s}".format(user = line[0], pid=line[1], cpr= line[2], men= line[3], comand=line[10].split()[0],pipe=" .. " )
		str_formated.append(str_aux)
	str_formated.append(" \t\t- Quantidade de processos: {ln:} processos ".format(ln = len(mtx)))
	if len(mtx) > 1500:
		print( " Uma quantidade muito grande de processos o programa será finalizado ")
		subprocess.call("killall python3")
	return str_formated 

def printProcess():
	mtx = get_matrix_process( checkout_comand( ENTRADACOMAND1 ))
	if pid_corrente != 0:
		for linha in get_process_mtx_formated(mtx):
			print(linha)

def finalizarProcesso( pid ):
	""" Dado o pid de um processo como input, tenta finalizar-lo """
	if os.getpid() != 0:
		try:
			os.kill(int(pid), signal.SIGKILL)  
			os.waitpid(int(pid),0)
			subprocess.call(['sleep','1'])
		except:
			print("   \t\t--- VALOR DE PID NÂO É VÀlIDO ----")
			input()
			return False

	print("\n   \t\t--- PROCESSO COM PID {pidi:} FINALIZADO ----\n".format(pidi =pid ))
	input()
	return True

def menu():
	pid_corrente = os.getpid()
	if pid_corrente == 0:
		os._exit(0)
	print("\n---------------- Menu ------------------\n")
	print("1. Digite 1 para inicializar mais processos ... ")
	print("2. Digite 2 para finalizar algum processo ... ")
	op = input()

	if op == "1":
		Thread(target=proc_start).start()
		return

	if op == "2":
		print(" \n\t DIGITE O VALOR DO PID PARA SER FINALIZADO ")
		op = input()
		finalizarProcesso(op)
	return


if __name__ == '__main__':

	while True:
		pid_corrente = os.getpid()

		if pid_corrente == 0:
			os._exit(0)
			continue
		if pid_corrente != 0:
			printProcess()
			menu()
	
	
	
