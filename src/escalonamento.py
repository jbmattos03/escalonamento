'''
Escalonador de processos
+ FIFO
+ SJF
+ Round Robin
+ Prioridade
+ EDF
'''

import sys
from collections import deque

# cadastrar processo
def processar_input(input_lines=None):
    lista_proc = []
    i = 0

    if input_lines is None:
        input_lines = sys.stdin.readlines()

    for linha in input_lines:
        #linha = input("Digite os valores de chegada, prioridade, deadline e tempo de execução separados por espaços \n")
        linha = linha.strip()

        if linha.lower() == "p": #condição de parada
            break

        linha = linha.split(" ") #separar os elementos da linha
        
        # checar se a linha tem 5 elementos
        if len(linha) != 4:
            print("Insira 4 valores separados por espaços \n")
            continue # ir para próxima iteração

        # checar tipo dos valores
        try:
            proc = {
                "chegada": int(linha[0]),
                "prioridade": int(linha[1]),
                "deadline": int(linha[2]),
                "tempo": int(linha[3])
            }    
        except ValueError:
            print("Insira apenas números ou \"p\" para parar \n")
            continue
        
        proc["id"] = i
        lista_proc.append(proc)

        i += 1

    if input_lines is None or not input_lines[-1].strip().isdigit():
        quantum = int(input("Digite o quantum \n")) # quantum
    else:
        quantum = int(input_lines.pop().strip())

    #quantum = int(input("Digite o valor do quantum \n"))

    return lista_proc, quantum
    #print(f'Quantum:" {quantum}\n')

# FIFO
def fifo(lista_proc):
    lista_proc.sort(key=lambda x: x["chegada"]) # ordenar por ordem chegada

    espera = 0
    tp_total = 0
    total_tempo = 0

    for i in range(len(lista_proc)):
        if i == 0: # primeiro processo
            total_tempo += lista_proc[i]["tempo"]
        else:
            espera = total_tempo - lista_proc[i]["chegada"] 

            total_tempo += lista_proc[i]["tempo"]

        tp_total += (espera + lista_proc[i]["tempo"])

    return tp_total / len(lista_proc)
    
#print(fifo(lista_proc))

def sjf(lista_proc):
    lista_proc.sort(key=lambda x: x["chegada"]) # organizar a lista por chegada
    
    total_tempo = 0
    tp_total = 0
    processos = lista_proc[:] # cópia da lista pra não atrapalhar os próximos processos

    while processos:
        next = [proc for proc in processos if proc["chegada"] <= total_tempo] # escolher o próximo processo a ser feito
        
        if next:
            min_tempo = min(next, key=lambda proc: proc["tempo"]) # pegada do tempo do processo escolhido
        else:
            min_tempo = min(processos, key=lambda proc: proc["chegada"]) # caso não há nenhum processo escolhido, chama o processo
            total_tempo = min_tempo["chegada"]                           # mais próximo e que seja o menor 
        
        espera = total_tempo - min_tempo["chegada"] # tempo de espera
        if espera < 0:
            espera = 0
        
        total_tempo += min_tempo["tempo"]  # adiciona o andamento do tempo que o processo está fazendo
        tp_total += espera + min_tempo["tempo"] # formação do turnaround
        processos.remove(min_tempo)  # remoção do processo na cópia da lista
    
    return tp_total / len(lista_proc)

#print(sjf(lista_proc))

#EDF
def edf(lista_proc, quantum):
    lista_proc.sort(key=lambda x: x["chegada"]) # organizar a lista por chegada
    
    total_tempo = 0
    tp_total = 0
    processos = lista_proc[:]
    sobrecarga = 0

    while processos:
        next = [proc for proc in processos if proc["chegada"] <= total_tempo] # procura o processo com menor tempo
        
        if next:
            min_deadline = min(next, key=lambda proc: proc["deadline"]) # procura o processo com menor deadline
        else:
            min_deadline = min(processos, key=lambda proc: proc["chegada"]) # chama o próximo processo se não tiver processos no tempo atual
            total_tempo = min_deadline["chegada"]                          
        
        tempo = int(min_deadline["tempo"])  # cálculo da sobrecarga
        while tempo > quantum:
            sobrecarga += 1
            tempo -= quantum
            total_tempo += quantum + 1

        total_tempo += tempo # tempo atual

        turnaround_time = (total_tempo - min_deadline["chegada"])
        tp_total += turnaround_time # turnaround
        
        processos.remove(min_deadline)  # remoção do processo na cópia da lista
    
    return tp_total / len(lista_proc)
    #return tp_total / len(lista_proc)

#print(edf(lista_proc, quantum))

# Round Robin
def round_robin(lista_proc, quantum):
    lista_proc.sort(key=lambda x: x["chegada"]) # ordenar a lista por chegada

    processos = lista_proc[:]
    total_tempo = 0
    tp_total = 0
    sobrecarga = 0

    while processos:
        prox = [proc for proc in processos if proc["chegada"] <= total_tempo]

        if prox:
            min_chegada = min(prox, key=lambda proc: proc["chegada"])
        else:
            min_chegada = min(processos, key=lambda proc: proc["chegada"])
            total_tempo = min_chegada["chegada"]
        
        tempo = int(min_chegada["tempo"])  # cálculo da sobrecarga
        while tempo > quantum:
            sobrecarga += 1
            tempo -= quantum
            total_tempo += quantum + 1

        total_tempo += tempo # tempo atual

        turnaround_time = (total_tempo - min_chegada["chegada"])
        tp_total += turnaround_time # turnaround
        
        processos.remove(min_chegada)  # remoção do processo na cópia da lista

    return tp_total / len(lista_proc)

#print(round_robin(lista_proc, quantum))