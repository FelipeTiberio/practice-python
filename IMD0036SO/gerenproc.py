import os, subprocess

teste1 = ['ps', '-C', 'python3']
teste2= 'ps -aux'

def checkout_sys_process( args  ):
	""" @return retorna todos os processos do sistema em uma linha 
		Para o sistema funcianr espera-se que o comando do sistema seja ps   """
	
	stdout = subprocess.check_output( args , shell=True)

	return stdout.decode()

def list_of_lines ( process ):
	"""@arg process, recebe uma string retorna uma lista onde cada item é uma 
		linha da string  """

	return process.split('\n')




#print(checkout_sys_process(teste))
debug = list_of_lines( checkout_sys_process( teste2 ))

print( "Tamanho de debug " + str(len(debug)))
for i in range(6) :
	print(debug[i])
