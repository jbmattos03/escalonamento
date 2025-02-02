import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def gantt(lista_proc, quantum, output):
    tasks = []
    current_time = 0

    for proc in lista_proc:
        start_time = current_time
        end_time = start_time + proc["tempo"]
        tasks.append({
            "Processo": f'P{lista_proc.index(proc) + 1}',
            "Início": start_time,
            "Fim": end_time,
        })
        current_time = end_time

    # converter tasks em DataFrame
    df = pd.DataFrame(tasks)

    # criar gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    _, ax = plt.subplots(figsize=(10, 6))
    for i, task in enumerate(tasks):
        ax.barh(y=task["Processo"], width=task["Fim"] - task["Início"], left=task["Início"], color=sns.color_palette("husl", len(tasks))[i], label=task["Processo"])

    ax.set_title("Gráfico de Gantt")
    ax.set_xlabel("Tempo")
    ax.set_ylabel("Processo")
    ax.set_xticks(range(0, sum(proc["tempo"] for proc in lista_proc) + 5, quantum))
    ax.legend()

    plt.savefig(output)
    plt.close()
