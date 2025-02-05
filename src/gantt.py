import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def gantt(processes, output):
    fig, ax = plt.subplots()
    cmap = plt.get_cmap("tab10")
    colors = cmap(np.linspace(0, 1, len(processes)))

    max = -1
    for proc in processes:
        if proc["end"] > max:
            max = proc["end"]

    for i, process in enumerate(processes):
        start_time = process["start"]
        end_time = process["end"]
        ax.barh(i, end_time - start_time, left=start_time, color=colors[i], edgecolor='black', label=f"Process {process['id'] + 1}")

    ax.set_xlabel("Tempo")
    ax.set_ylabel("Processos")
    ax.set_title("Gantt Chart")
    ax.set_yticks(np.arange(len(processes)))
    ax.set_yticklabels([f"Processo {process['id'] + 1}" for process in processes])
    ax.set_xlim(0, max + 5)
    ax.legend(loc="upper right")
    ax.grid(True)

    plt.tight_layout()
    plt.savefig(output)
    plt.close()
