import  subprocess, os
teste2= 'ps -au'
#teste2= 'ps -aux'

def proc_start():
	""" Inicializa um novo processo filho retornando o pid correspondente ao 
	processo criado """
	if os.getpid() != 0: # Zero significa que é a cópia
		newpid = os.fork()
	if newpid != 0:
		print( " ** Processo com pid", newpid, "criado. ")	
	if newpid == 0:
		os._exit(0)
		return

	return newpid

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

def get_process( mtx, user ='all' , amount = -1, fullinfo = True):
	""" @arg user, imprime apenas os processo de user
		@arg amout, imprime os amount's primeiros processos
		@arg fullinfo, Quando False, retorna apenas uma quantidade minima de informações de cada processo 
			já quando True impre todo o retorno do comando ps -flag
	"""
	is_first_line  = True
	str_formated = []

	for line in mtx:
		for i in range(len(line)):
			if user == 'all' and fullinfo:
				str_aux = "| {user:12s} {pid:5s} {men:5s} {comand:56s} {pipe:5s}".format(user = line[0], pid=line[1], cpr= line[2], men= line[3], comand=line[10].split()[0],pipe="|" )
		str_formated.append(str_aux)

	return str_formated 
			
### debug 
mtx = get_matrix_process( checkout_comand( teste2 ))
x = 0


while True:
	if os.getpid() == 0:
		continue

	if os.getpid() != 0:
		for i in get_process(mtx):
			print(i)
			if( x >= 10):
				break
			x+=1

		print(" Vc quer criar mais um processo ?")
		entrada = input()

		if entrada == "s":
			proc_start()
		else:
			continue

			


	
		