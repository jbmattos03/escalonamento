'''
Escalonador de processos
+ FIFO
+ SJF
+ Round Robin
+ Prioridade
+ EDF
'''

# cadastrar processo
lista_proc = []

while True:
    linha = input("Digite uma linha (ou \"p\" para parar) \n")

    if linha.lower() == "p": #condição de parada
        break

    linha = linha.split(" ") #separar os elementos da linha
    
    # checar se a linha tem 3 elementos
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

    lista_proc.append(proc)
    
quantum = int(input("Digite o quantum \n")) # quantum

print(lista_proc)
print(f'Quantum:" {quantum}\n')

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

print(edf(lista_proc, quantum))