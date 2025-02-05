'''
Escalonador de processos
+ FIFO
+ SJF
+ Round Robin
+ Prioridade
+ EDF
'''

from collections import deque

# FIFO
def fifo(lista_proc):
    lista_proc.sort(key=lambda x: x["chegada"]) # ordenar por ordem chegada

    espera = 0
    tp_total = 0
    total_tempo = 0
    lista_res = []

    for i in range(len(lista_proc)):
        if i == 0: # primeiro processo
            total_tempo += lista_proc[i]["tempo"]
        else:
            espera = total_tempo - lista_proc[i]["chegada"] 

            total_tempo += lista_proc[i]["tempo"]

        tp_total += (espera + lista_proc[i]["tempo"])

        proc = {
            "id": lista_proc[i]["id"],
            "start": lista_proc[i]["chegada"] + espera,
            "end": lista_proc[i]["chegada"] + espera + lista_proc[i]["tempo"]
        }

        lista_res.append(proc)

    return lista_res, tp_total / len(lista_proc)
    
#print(fifo(lista_proc))

def sjf(lista_proc):
    lista_proc.sort(key=lambda x: x["chegada"]) # organizar a lista por chegada
    
    total_tempo = 0
    tp_total = 0
    processos = lista_proc[:] # cópia da lista pra não atrapalhar os próximos processos
    lista_res = []

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
        
        proc = {
            "id": min_tempo["id"],
            "start": total_tempo,
            "end": total_tempo + espera + min_tempo["tempo"]
        }

        lista_res.append(proc) # adicionar o processo na lista de resultados
        
        total_tempo += min_tempo["tempo"]  # adiciona o andamento do tempo que o processo está fazendo
        tp_total += espera + min_tempo["tempo"] # formação do turnaround
        processos.remove(min_tempo)  # remoção do processo na cópia da lista
    
    return lista_res, tp_total / len(lista_proc)

#print(sjf(lista_proc))

# Prioridade
def prioridade(lista_proc, quantum):
    lista_proc.sort(key=lambda x: x["chegada"]) # organizar a lista por chegada
    
    total_tempo = 0
    tp_total = 0
    processos = lista_proc[:]
    sobrecarga = 0
    lista_res = []

    while processos:
        next = [proc for proc in processos if proc["chegada"] <= total_tempo] # procura o processo com menor tempo
        
        if next:
            max_prioridade = max(next, key=lambda proc: proc["prioridade"]) # procura o processo com maior prioridade
        else:
            max_prioridade = min(processos, key=lambda proc: proc["chegada"]) # chama o próximo processo se não tiver processos no tempo atual
            total_tempo = max_prioridade["chegada"]  

        proc = {
            "id": max_prioridade["id"],
            "start": total_tempo,
        }                        
        
        tempo = int(max_prioridade["tempo"])  # cálculo da sobrecarga
        while tempo > quantum:
            sobrecarga += 1
            tempo -= quantum
            total_tempo += quantum + 1
        
        proc["end"] = total_tempo + max_prioridade["tempo"]

        lista_res.append(proc) # adicionar o processo na lista de resultados
        
        total_tempo += tempo # tempo atual

        turnaround_time = (total_tempo - max_prioridade["chegada"])
        tp_total += turnaround_time # turnaround
        
        processos.remove(max_prioridade)  # remoção do processo na cópia da lista
    
    return lista_res, tp_total / len(lista_proc)

# EDF
def edf(lista_proc, quantum):
    lista_proc.sort(key=lambda x: x["chegada"]) # organizar a lista por chegada
    
    total_tempo = 0
    tp_total = 0
    processos = lista_proc[:]
    sobrecarga = 0
    lista_res = []

    while processos:
        next = [proc for proc in processos if proc["chegada"] <= total_tempo] # procura o processo com menor tempo
        
        if next:
            min_deadline = min(next, key=lambda proc: proc["deadline"]) # procura o processo com menor deadline
        else:
            min_deadline = min(processos, key=lambda proc: proc["chegada"]) # chama o próximo processo se não tiver processos no tempo atual
            total_tempo = min_deadline["chegada"]  

        proc = {
            "id": min_deadline["id"],
            "start": total_tempo,
        }                        
        
        tempo = int(min_deadline["tempo"])  # cálculo da sobrecarga
        while tempo > quantum:
            sobrecarga += 1
            tempo -= quantum
            total_tempo += quantum + 1
        
        proc["end"] = total_tempo + min_deadline["tempo"]

        lista_res.append(proc) # adicionar o processo na lista de resultados
        
        total_tempo += tempo # tempo atual

        turnaround_time = (total_tempo - min_deadline["chegada"])
        tp_total += turnaround_time # turnaround
        
        processos.remove(min_deadline)  # remoção do processo na cópia da lista
    
    return lista_res, tp_total / len(lista_proc)
    #return tp_total / len(lista_proc)

#print(edf(lista_proc, quantum))

# Round Robin
def round_robin(lista_proc, quantum):
    lista_proc.sort(key=lambda x: x["chegada"]) # ordenar a lista por chegada

    processos = lista_proc[:]
    total_tempo = 0
    tp_total = 0
    sobrecarga = 0
    lista_res = []

    while processos:
        prox = [proc for proc in processos if proc["chegada"] <= total_tempo] # processos que chegaram

        if prox:
            min_chegada = min(prox, key=lambda proc: proc["chegada"]) # escolher o próximo processo dos que chegaram
        else:
            min_chegada = min(processos, key=lambda proc: proc["chegada"]) # caso não tenha processo, chama o próximo processo que chegar
            total_tempo = min_chegada["chegada"]

        proc = {
            "id": min_chegada["id"],
            "start": total_tempo,
        }
        
        tempo = int(min_chegada["tempo"])  # cálculo da sobrecarga
        while tempo > quantum:
            sobrecarga += 1
            tempo -= quantum
            total_tempo += quantum + 1

        proc["end"] = total_tempo + min_chegada["tempo"]

        lista_res.append(proc) # adicionar o processo na lista de resultados
        
        total_tempo += tempo # tempo atual

        turnaround_time = (total_tempo - min_chegada["chegada"])
        tp_total += turnaround_time # turnaround
        
        processos.remove(min_chegada)  # remoção do processo na cópia da lista

    return lista_res, tp_total / len(lista_proc)

#print(round_robin(lista_proc, quantum))