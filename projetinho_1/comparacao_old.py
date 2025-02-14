import random
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from tabulate import tabulate
from forca_bruta import par_mais_proximo_forca_bruta
from divisao_conquista import par_mais_proximo_divisao_conquista

def gerar_pontos(n):
    """Gera um conjunto de n pontos 2D aleatórios com coordenadas entre -2n e 2n."""
    limite = 2 * n
    return [(random.randint(-limite, limite), random.randint(-limite, limite)) for _ in range(n)]

# Gerar entre 100 e 200 valores de n aleatórios entre 10 e 10.000, distribuídos logaritmicamente
k = random.randint(100, 200)
n_values = sorted(set(map(int, np.logspace(1, 3.5, k))))  # Escala logarítmica

# Número de execuções para cada tamanho de entrada
m = random.randint(10, 20)

# Dicionários para armazenar tempos de execução
tempos_forca_bruta = {}
tempos_divisao_conquista = {}

for n in n_values:
    total_tempo_fb = 0
    total_tempo_dc = 0
    diferencas = 0

    for _ in range(m):
        pontos = gerar_pontos(n)
        
        # Executa Força Bruta
        inicio = time.time()
        _, _, dist_fb = par_mais_proximo_forca_bruta(pontos)
        fim = time.time()
        total_tempo_fb += (fim - inicio)
        
        # Executa Divisão e Conquista
        inicio = time.time()
        _, _, dist_dc = par_mais_proximo_divisao_conquista(pontos)
        fim = time.time()
        total_tempo_dc += (fim - inicio)
        
        # Verifica se os resultados são diferentes
        if abs(dist_fb - dist_dc) > 1e-6:
            diferencas += 1
            print(f"n = {n}, Diferença detectada!")
            print(f"  - Força Bruta: {dist_fb:.10f}")
            print(f"  - Divisão e Conquista: {dist_dc:.10f}")

    # Armazena os tempos médios
    tempos_forca_bruta[n] = total_tempo_fb / m
    tempos_divisao_conquista[n] = total_tempo_dc / m

    if diferencas > 0:
        print(f"Aviso: {diferencas} diferenças encontradas para n = {n}")

# Criar DataFrame para facilitar a manipulação dos dados
df = pd.DataFrame({
    'Tamanho Entrada (n)': n_values,
    'Força Bruta': [tempos_forca_bruta[n] for n in n_values],
    'Divisão e Conquista': [tempos_divisao_conquista[n] for n in n_values]
})

# Adicionar a razão de tempo (FB/DC)
df['Razão (FB/DC)'] = df['Força Bruta'] / df['Divisão e Conquista']

# Legenda antes da tabela
print("\n=== INTERPRETAÇÃO DA TABELA ===")
print("- Coluna 'n': tamanho da entrada (quantidade de pontos)")
print("- Coluna 'Tempo Força Bruta (s)': tempo médio de execução do algoritmo de Força Bruta")
print("- Coluna 'Tempo Divisão e Conquista (s)': tempo médio de execução do algoritmo de Divisão e Conquista")
print("- Coluna 'Razão (FB/DC)': quantas vezes a Força Bruta foi mais lenta que a Divisão e Conquista")
print("  - Se for maior que 1: Força Bruta foi mais lenta")
print("  - Se for aproximadamente 1: tempos semelhantes")
print("  - Se for 'inf': o tempo de Divisão e Conquista foi tão pequeno que a divisão gerou infinito")
print("=================================\n")

# 📋 4. Tabela Comparativa no Console
headers = ["n", "Tempo Força Bruta (s)", "Tempo Divisão e Conquista (s)", "Razão (FB/DC)"]
print(tabulate(df.values, headers=headers, tablefmt="github"))

# 💾 Opcional: Salvar os resultados em CSV para análise posterior
df.to_csv("comparacao_tempos.csv", index=False)

# Conclusão Final:
# ✅ Para n pequeno, os tempos são tão rápidos que podem aparecer como 0.0, resultando em valores inf para Razão FB/DC.
# ✅ Conforme n cresce, a Força Bruta se torna extremamente lenta em comparação com a Divisão e Conquista.
# ✅ A Razão FB/DC cresce exponencialmente, confirmando que a Força Bruta é O(n^2) e a Divisão e Conquista é O(nlogn).
# ✅ Para valores grandes de n, a Força Bruta pode levar mais de 50x o tempo da Divisão e Conquista!


# 📊 1. Boxplot - Distribuição dos Tempos
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['Força Bruta', 'Divisão e Conquista']])
plt.title("Distribuição dos Tempos de Execução")
plt.ylabel("Tempo (s)")
plt.grid()
plt.show()

# 📈 2. Gráfico de Dispersão com Ajuste de Regressão
sns.lmplot(x='Tamanho Entrada (n)', y='Força Bruta', data=df, ci=None, order=2)
plt.title("Tendência de Crescimento - Força Bruta")
plt.show()

sns.lmplot(x='Tamanho Entrada (n)', y='Divisão e Conquista', data=df, ci=None, order=2)
plt.title("Tendência de Crescimento - Divisão e Conquista")
plt.show()

# 📉 3. Gráfico de Razão Logarítmica
plt.figure(figsize=(8, 5))
plt.plot(df['Tamanho Entrada (n)'], df['Razão (FB/DC)'], marker='o', linestyle='--', color='purple')
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Tamanho da Entrada (n)")
plt.ylabel("Razão de Tempo (Força Bruta / Divisão e Conquista)")
plt.title("Comparação de Eficiência em Escala Logarítmica")
plt.grid()
plt.show()

# 📋 4. Tabela Comparativa no Console
headers = ["n", "Tempo Força Bruta (s)", "Tempo Divisão e Conquista (s)", "Razão (FB/DC)"]
print(tabulate(df.values, headers=headers, tablefmt="github"))

# 💾 Opcional: Salvar os resultados em CSV para análise posterior
df.to_csv("comparacao_tempos.csv", index=False)

