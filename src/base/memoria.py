lista_subs = list(map(int, input("Coloque no máximo 10 elementos/páginas:\n").split()))

if len(lista_subs) > 10:
     print("Erro, tem mais que 10 elementos")
     exit()

num_paginas = int(input("Quantas páginas estarão disponíveis: \n"))

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
    
        print(f"Páginas {pagina}: {memoria}")

    return memoria

print("Última página:",subs_pag_fifo(lista_subs, num_paginas))