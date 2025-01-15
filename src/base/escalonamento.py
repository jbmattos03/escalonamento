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