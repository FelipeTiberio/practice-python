import  subprocess

#teste2 = ['ps', '-C', 'python3']
teste2= 'ps -aux'

def checkout_comand( args  ):
	""" retorna todos os processo do sisteam em uma lista, cada item da lista é uma linha do comando args   """
	stdout = subprocess.check_output( args , shell=True)
	return stdout.decode().split('\n')

def get_matrix_process( str_lines ):
	""" retorna uma matriz com o texo recebido """
	matrix = []
	maxsplit = (len(str_lines[0].split()))-1 # a quantidade de colunas de matrix sera os rotulos do output de subprocess(ps)
	
	for line in str_lines: # criando a matrix com a saida de ps 
		matrix.append( line.split( maxsplit= maxsplit ))

	return matrix

def get_process( mtx, user = all , amount = -1, fullinfo = False):
	""" @arg user, imprime apenas os processo de user
		@arg amout, imprime os amount's primeiros processos
		@arg fullinfo, Quando False, retorna apenas uma quantidade minima de informações de cada processo 
			já quando True impre todo o retorno do comando ps -flag
	"""


mtx = get_matrix_process( checkout_comand( teste2 ))


for i in range(10):
	print(mtx[i])


	
	
			
#for i in checkout_comand( teste2 ):
#	print(i)
			

#txt = "welcome to the jungle"

#x = txt.split( maxsplit=1)

#print(x)


	
		