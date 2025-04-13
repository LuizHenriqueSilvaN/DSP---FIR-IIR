import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime  # Substitui a biblioteca 'time' por 'datetime'

def DFT_matricial(x, N):
    """Calcula a DFT de um sinal x usando o método matricial."""
    k = np.arange(N)
    n = np.arange(N)
    exponent = -2j * np.pi * np.outer(k, n) / N
    W = np.exp(exponent)
    return W @ x

# Valores de N: potências de 2 de 2 até 1024
N_values = [2**i for i in range(1, 11)]  # 2, 4, 8, ..., 1024
tempos = []

for N in N_values:
    x = np.random.rand(N)
    start = datetime.now()  # Marca o início com datetime
    _ = DFT_matricial(x, N)
    end = datetime.now()    # Marca o fim com datetime
    tempo_exec = (end - start).total_seconds()  # Calcula a diferença em segundos
    tempos.append(tempo_exec)
    print(f"N={N}: Tempo = {tempo_exec:.6f} segundos")
    print (x)


# Plotagem do gráfico (mesmo código anterior)
plt.figure(figsize=(10, 6))
plt.plot(N_values, tempos, 'o-', markersize=5)
plt.xlabel('N (Tamanho da Transformada)')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de Execução da DFT Matricial usando VS Code')
plt.xscale('log', base=2)
plt.yscale('log')
plt.grid(True, which='both', linestyle='--')
plt.xticks(N_values, labels=N_values)
plt.show()