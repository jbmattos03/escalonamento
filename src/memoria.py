from processar_input import processar_input_m
import sys

def subs_pag_fifo(lista_subs, num_paginas):
    memoria = []  # lista para a memória
    lista = lista_subs[:] # cópia da lista
    pagina = 0
    for page in lista:
        if page in memoria: # se a página já estiver na memória, vai para a próxima
            continue
        if page not in memoria and len(memoria) < num_paginas : # se a página não estiver na memória, e tiver espaço, ele adiciona
                memoria.append(page) 
                pagina += 1
        else: #se a página não estiver na memória e não tiver espaço, ele apaga o elemento a entrar primeiro e adiciona
             memoria.pop(0)
             memoria.append(page)
             pagina += 1
    
        #print(f"Páginas {pagina}: {memoria}")

    return memoria

#print("Última página do FIFO:",subs_pag_fifo(lista_subs, num_paginas))

def lru(lista_subs, num_paginas):
    memoria = [] # lista para a memória
    lista = lista_subs[:] # cópia da lista
    pagina = 0
    for page in lista:
        if page in memoria: # se a página já estiver na memória, ele apaga e entra novamente para ser a página mais recente
            memoria.remove(page)
            memoria.append(page)
            pagina += 1
        else: 
            if len(memoria) >= num_paginas : # se não estiver na memória, ele apaga a memória menos referenciada recentemente, e adiciona outra página
                memoria.pop(0)
            memoria.append(page)
            pagina += 1
    
        #print(f"Páginas {pagina}: {memoria}")

    return memoria

#print("Última página do:", lru(lista_subs, num_paginas))