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

print(lista_proc)

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
    
print(fifo(lista_proc))

# SJF
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

print(sjf(lista_proc))