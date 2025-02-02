from entradateste import processar_input_m
import sys

def subs_pag_fifo(lista_subs, num_paginas):
    memoria = []
    lista = lista_subs[:]
    pagina = 0
    for page in lista:
        if page in memoria:
            continue
        if page not in memoria and len(memoria) < num_paginas :
                memoria.append(page)
                pagina += 1
        else:
             memoria.pop(0)
             memoria.append(page)
             pagina += 1
    
        #print(f"Páginas {pagina}: {memoria}")

    return memoria

#print("Última página do FIFO:",subs_pag_fifo(lista_subs, num_paginas))

def lru(lista_subs, num_paginas):
    memoria = []
    lista = lista_subs[:]
    reference = lista_subs[:]
    pagina = 0
    for page in lista:
        if page in memoria:
            memoria.remove(page)
            memoria.append(page)
            pagina += 1
        else: 
            if len(memoria) >= num_paginas :
                memoria.pop(0)
            memoria.append(page)
            pagina += 1
    
        #print(f"Páginas {pagina}: {memoria}")

    return memoria

#print("Última página do:", lru(lista_subs, num_paginas))