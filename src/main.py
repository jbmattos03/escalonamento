from escalonamento import fifo, sjf, edf, round_robin, processar_input
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'file':
        with open('in.txt', 'r') as infile:
            input_lines = infile.readlines()
            lista_proc, quantum = processar_input(input_lines)
    else:
        input_lines = sys.stdin.readlines()
        lista_proc, quantum = processar_input(input_lines)

    with open('out.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(f"FIFO: {fifo(lista_proc)}\n")
        outfile.write(f"SJF: {sjf(lista_proc)}\n")
        outfile.write(f"EDF: {edf(lista_proc, quantum)}\n")
        outfile.write(f"Round Robin: {round_robin(lista_proc, quantum)}\n")


if __name__ == "__main__":
    main()