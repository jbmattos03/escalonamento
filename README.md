# Escalonamento
Solução para o trabalho final da disciplina Sistemas Operacionais.

Equipe: Júlia Mattos e Thiago Dias


# FASE 1) 
Considere um sistema operacional que implementa escalonamento de processos. O funcionamento esperado é que esse ambiente tenha N processos que podem chegar em tempos distintos para execução. Para cada processo, deve ser informado manualmente:
+ Tempo de chegada  
+ Tempo de execução
+ Deadline
+ Quantum do sistema
+ Sobrecarga do sistema

É necessário guardar essas informações, de tal forma que não seja necessário repetir esses dados de entrada quando for trocado o algoritmo de escalonamento.

Esse sistema deve implementar os algoritmos de escalonamento:  
+ FIFO
+ SJF
+ Round Robin
+ EDF

# FASE 2) 
Esse sistema deve implementar os algoritmos de substituição de páginas:
+ FIFO
+ Menos Recentemente Utilizada

# Requisitos: 
+ Cada processo deve ter até 10 páginas (entrada do usuário). Cada página tem 4K de tamanho. A RAM tem 200 K de memória.
+ Crie a abstração de DISCO para utilização da memória virtual. Caso ocorra falta de página, utilize N u.t. para o uso do Disco. 
+ O grupo está livre para a criação de qualquer abstração extra que se mostrar necessária.
+ Deve-se criar o gráfico de uso da RAM e do Disco, mostrando as páginas presentes em tempo-real.
+ Os processos só executam se todas as suas páginas estiverem na RAM.
+ Deve-se criar o gráfico de Gantt para mostrar as execuções dos processos, visualização da CPU e da RAM
+ A resposta deve ser dada em função do turnaround médio (tempo de espera + tempo de execução)
+ Colocar delay para verificar a execução 
+ Para os testes, favor não apagar os dados de entrada a cada execução.
+ A linguagem de programação é de escolha do grupo.

# Como Rodar
Primeiro, certifique-se de que está no diretório src com:

```
cd src
```

Então. execute os seguintes comandos no seu terminal:

```
py main.py file
```

```
py main2.py
```

