from escalonamento import fifo, sjf, edf, prioridade, round_robin
from processar_input import processar_input, processar_input_m
from memoria import subs_pag_fifo, lru
from gantt import gantt
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "file":
        with open("in.txt", "r", encoding="utf-8") as infile:
            input_lines = infile.readlines()
            lista_proc, quantum = processar_input(input_lines)
    else:
        input_lines = sys.stdin.readlines()
        lista_proc, quantum = processar_input(input_lines)

    lista_proc_fifo, res_fifo = fifo(lista_proc)
    gantt(lista_proc_fifo, "fifo.png")

    lista_proc_sjf, res_sjf = sjf((lista_proc))
    gantt(lista_proc_sjf,  "sjf.png")

    lista_proc_edf, res_edf = edf(lista_proc, quantum)
    gantt(lista_proc_edf, "edf.png")

    lista_proc_pr, res_pr = prioridade(lista_proc, quantum)
    gantt(lista_proc_pr, "prioridade.png")

    lista_proc_rr, res_rr = round_robin(lista_proc, quantum)
    gantt(lista_proc_rr, "rr.png")

    with open("out.txt", "w", encoding="utf-8") as outfile:
        outfile.write(f"FIFO: {res_fifo}\n")
        outfile.write(f"SJF: {res_sjf}\n")
        outfile.write(f"EDF: {res_edf}\n")
        outfile.write(f"Prioridade: {res_pr}\n")
        outfile.write(f"Round Robin: {res_rr}\n")

if __name__ == "__main__":
    main()