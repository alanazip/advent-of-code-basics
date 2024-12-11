import pandas as pd
import matplotlib.pyplot as plt

# Dados simulados
data = {
    "Equipe": ["Administração", "Marketing", "TI", "RH"],
    "Planejamento (Horas)": [10, 8, 6, 12],
    "Reuniões (Horas)": [15, 12, 10, 8],
    "Execução (Horas)": [20, 25, 30, 15],
    "Revisão (Horas)": [5, 10, 8, 5],
}

# Criando um DataFrame
df = pd.DataFrame(data)

# Configurando o gráfico
df.set_index("Equipe").plot(kind="bar", figsize=(10, 6))
plt.title("Distribuição de Horas por Equipe e Tarefa")
plt.ylabel("Horas")
plt.xlabel("Equipes")
plt.legend(title="Tarefas")
plt.tight_layout()

# Exibindo o gráfico
plt.show()