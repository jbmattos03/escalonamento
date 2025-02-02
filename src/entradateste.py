import sys

def processar_input_m(input_lines_m=None):
    lista_subs = []

    if input_lines_m is None:
        input_lines_m = sys.stdin.readlines()

    input_lines_m = [linha.strip() for linha in input_lines_m if linha.strip()]

    try:
        lista_subs = list(map(int, input_lines_m[:-1]))  # Todas as linhas, exceto a última
        num_paginas = int(input_lines_m[-1])  # Última linha contém o número de páginas
    except ValueError:
        print("Erro: Insira apenas números inteiros.")
        return None

    if len(lista_subs) > 10:
        print("Erro: mais de 10 elementos na lista.")
        return None

    return lista_subs, num_paginas