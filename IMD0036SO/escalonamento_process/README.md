 - [x] (O primeiro algoritmo a ser implementado é o Round-Robin (ou circular),
       onde os processos são executados um atrás do outro e não uso de prioridades. 
       O primeiro processo depois de executado deverá retornar para o final da fila.)

 - [ ] (O segundo algoritmo a ser implementado é o Por Prioridades, onde existem diversas
    classes de prioridades de processos , onde os processos dentro dessa classe são
    executados de forma circular. A  classe com prioridade mais alta deve ser executada 
    primeiro antes das outras, e, as outras só poderam ser executadas quando a
    classe de prioridade maior acabar com os seus processos, a não ser que aja algum controle para evitar starvation.)

 - [x] (Deverão ser utilizadas pelo menos 3 threads para a realização da tarefa.)

 - [x] (Os programas deverão conter além dos algoritmos de escalonamento uma função CPU onde deverá receber 
       como parâmetro uma thread e iniciar a sua execução.)

 - [x] Cada função que as threadas estarão executando receberão como parâmetro um número, 
    esse número deverá ser o tempo que a thread vai executar, simbolizando o tempo que ela tem 
    dentro da CPU. Quando esse tempo acaba o algortimo de escalonamento deverá escolher uma outra
    thread para ser executada pela CPU, chamando a função CPU novamente e passando a thread escolhida como parâmetro.



    ----------------------------
       Múltiplas Filas[7][8]: São usadas várias filas de processos prontos para executar, cada processo é colocado em uma fila, e cada fila tem uma política de escalonamento própria e outra entre filas, preemptivo, cada fila tem um determinado nível de prioridade, sendo um dos mais antigos agendadores de prioridade, estava presente no CTSS (Compatible Time-Sharing System - Sistema Compatível de Divisão por Tempo).No algoritmo de Múltiplas Filas, também pode ser aplicado particularmente, em cada fila, diferentes algoritmos como por exemplo, o algoritmo RR ou FCFS.

      Para que o processo em uma fila seja executado, todas as filas de prioridade mais altas do que deveriam estar vazias, o que significa que o processo nessas filas de alta prioridade deve ter concluído sua execução. Nesse algoritmo de agendamento, uma vez atribuído a uma fila, o processo não será movido para nenhuma outra fila.

      ##Problemas


      Starvation: Para evitar esse problema, o Sistema Operacional pode aplicar prioridades dinâmicas. Neste caso, os processos que não tiveram acesso à CPU durante muito tempo, têm sua prioridade momentaneamente elevada. Em sistemas interativos esse mesmo mecanismo também pode ser empregado, porque o usuário deve possuir uma prioridade alta para poder trocar de programa quando desejar.



      https://pt.wikipedia.org/wiki/M%C3%BAltiplas_filas


