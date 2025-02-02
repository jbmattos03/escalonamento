from escalonamento import fifo, sjf, edf, round_robin, processar_input
from gantt import gantt
import sys
import copy

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "file":
        with open("in.txt", "r", encoding="utf-8") as infile:
            input_lines = infile.readlines()
            lista_proc, quantum = processar_input(input_lines)
    else:
        input_lines = sys.stdin.readlines()
        lista_proc, quantum = processar_input(input_lines)

    lista_alg = {"FIFO": None, "SJF": None, "EDF": None, "Round Robin": None}

    # Make deep copies of lista_proc for each algorithm
    lista_proc_fifo = copy.deepcopy(lista_proc)
    lista_proc_sjf = copy.deepcopy(lista_proc)
    lista_proc_edf = copy.deepcopy(lista_proc)
    lista_proc_rr = copy.deepcopy(lista_proc)

    lista_alg["FIFO"] = fifo(lista_proc_fifo)
    gantt(lista_proc_fifo, quantum, "fifo.png")
        
    lista_alg["SJF"] = sjf(lista_proc_sjf)
    gantt(lista_proc_sjf, quantum, "sjf.png")

    avg_waiting_time_edf = edf(lista_proc_edf, quantum)
    lista_alg["EDF"] = avg_waiting_time_edf
    gantt(lista_proc_edf, quantum, "edf.png")

    avg_waiting_time_rr = round_robin(lista_proc_rr, quantum)
    lista_alg["Round Robin"] = avg_waiting_time_rr
    gantt(lista_proc_rr, quantum, "rr.png")

    with open("out.txt", "w", encoding="utf-8") as outfile:
        outfile.write(f"FIFO: {lista_alg.get('FIFO')}\n")
        outfile.write(f"SJF: {lista_alg.get('SJF')}\n")
        outfile.write(f"EDF: {lista_alg.get('EDF')}\n")
        outfile.write(f"Round Robin: {lista_alg.get('Round Robin')}\n")

if __name__ == "__main__":
    main()