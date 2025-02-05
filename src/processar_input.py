import sys

def processar_input(input_lines=None):
    lista_proc = []
    i = 0

    if input_lines is None:
        input_lines = sys.stdin.readlines()

    while i < len(input_lines):
        linha = input_lines[i].strip()

        if linha.lower() == "p":  # condição de parada
            break

        linha = linha.split(" ")  # separar os elementos da linha

        # checar se a linha tem 4 elementos
        if len(linha) != 4:
            print("Insira 4 valores separados por espaços \n")
            continue  # ir para próxima iteração

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

        proc["id"] = len(lista_proc)
        lista_proc.append(proc)

        i += 1

    # pegar valor do quantum
    if input_lines:
        quantum_line = input_lines[-1].strip()
        try:
            quantum = int(quantum_line)
        except ValueError:
            print("Insira um número inteiro para o quantum \n")
            quantum = int(input("Digite o quantum \n"))  # Prompt user for quantum if invalid
    else:
        quantum = int(input("Digite o quantum \n"))  # Prompt user for quantum if no input lines

    return lista_proc, quantum

def processar_input_m(input_lines_m=None):
    lista_subs = []

    if input_lines_m is None:
        input_lines_m = sys.stdin.readlines() # ler as linhas do bloco de notas

    input_lines_m = [linha.strip() for linha in input_lines_m if linha.strip()] # verificar cada linha

    try:
        lista_subs = list(map(int, input_lines_m[:-1]))  # ela vai ler toda a lista de páginas
        num_paginas = int(input_lines_m[-1])  # ler quantas páginas podem entrar dentro da memória
    except ValueError:
        print("Erro: Insira apenas números inteiros.") # caso houver alguma letra
        return None

    if len(lista_subs) > 10:
        print("Erro: mais de 10 elementos na lista.") # caso houver mais de algum número
        return None

    return lista_subs, num_paginas