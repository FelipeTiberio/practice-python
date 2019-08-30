 - [] (O primeiro algoritmo a ser implementado é o Round-Robin (ou circular),
       onde os processos são executados um atrás do outro e não uso de prioridades. 
       O primeiro processo depois de executado deverá retornar para o final da fila.)
 - [] (O segundo algoritmo a ser implementado é o Por Prioridades, onde existem diversas
    classes de prioridades de processos , onde os processos dentro dessa classe são
    executados de forma circular. A  classe com prioridade mais alta deve ser executada 
    primeiro antes das outras, e, as outras só poderam ser executadas quando a
    classe de prioridade maior acabar com os seus processos, a não ser que aja algum controle para evitar starvation.)

 - [] (Deverão ser utilizadas pelo menos 3 threads para a realização da tarefa.)

 - [] (Os programas deverão conter além dos algoritmos de escalonamento uma função CPU onde deverá receber 
       como parâmetro uma thread e iniciar a sua execução.)
 - [] Cada função que as threadas estarão executando receberão como parâmetro um número, 
    esse número deverá ser o tempo que a thread vai executar, simbolizando o tempo que ela tem 
    dentro da CPU. Quando esse tempo acaba o algortimo de escalonamento deverá escolher uma outra
    thread para ser executada pela CPU, chamando a função CPU novamente e passando a thread escolhida como parâmetro.
