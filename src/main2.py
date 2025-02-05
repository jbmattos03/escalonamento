from memoria import subs_pag_fifo, lru
from processar_input import processar_input_m
import sys

def main2():
    if len(sys.argv) > 1 and sys.argv[1] == 'file':
        with open('inm.txt', 'r') as infile: # procura o texto de entrada
            input_lines_m = infile.readlines()
            lista_subs, num_paginas = processar_input_m(input_lines_m)
    else:
        input_lines_m = sys.stdin.readlines() # caso seja necessário, colocar manualmente
        lista_subs, num_paginas = processar_input_m(input_lines_m) 

    with open('outm.txt', 'w', encoding='utf-8') as outfile: # coloca a saída no txt necessário
        outfile.write(f"Última página da memória do FIFO: {subs_pag_fifo(lista_subs, num_paginas)}\n")
        outfile.write(f"Última página da memória do LRU: {lru(lista_subs, num_paginas)}\n")

if __name__ == "__main__":
    main2()