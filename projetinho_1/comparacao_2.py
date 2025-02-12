import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from forca_bruta import par_mais_proximo_forca_bruta
from divisao_conquista import par_mais_proximo_divisao_conquista

def gerar_pontos(n):
    """Gera um conjunto de n pontos 2D aleatórios com coordenadas entre -2n e 2n."""
    limite = 2 * n
    return [(random.randint(-limite, limite), random.randint(-limite, limite)) for _ in range(n)]

def comparar_algoritmos(n_values, m):
    """Compara os algoritmos de força bruta e divisão e conquista para diferentes tamanhos de entrada."""
    tempos_forca_bruta = {}
    tempos_divisao_conquista = {}
    diferencas_por_n = {}

    for n in n_values:
        total_tempo_fb = 0
        total_tempo_dc = 0
        diferencas = 0

        for _ in range(m):
            pontos = gerar_pontos(n)

            # Executa Força Bruta
            inicio = time.time()
            p1_fb, p2_fb, dist_fb = par_mais_proximo_forca_bruta(pontos)
            fim = time.time()
            total_tempo_fb += (fim - inicio)

            # Executa Divisão e Conquista
            inicio = time.time()
            p1_dc, p2_dc, dist_dc = par_mais_proximo_divisao_conquista(pontos)
            fim = time.time()
            total_tempo_dc += (fim - inicio)

            # Verifica se os resultados são diferentes
            if abs(dist_fb - dist_dc) > 1e-6:
                diferencas += 1

        # Armazena os tempos médios e o número de diferenças
        tempos_forca_bruta[n] = total_tempo_fb / m
        tempos_divisao_conquista[n] = total_tempo_dc / m
        diferencas_por_n[n] = diferencas

        # Exibir avisos de diferenças nos resultados
        if diferencas > 0:
            print(f"Aviso: {diferencas} diferenças encontradas para n = {n}")

    return tempos_forca_bruta, tempos_divisao_conquista, diferencas_por_n

def animar_grafico(n_values, tempos_forca_bruta, tempos_divisao_conquista):
    """Cria uma animação do gráfico de tempo de execução."""
    fig, ax = plt.subplots(figsize=(10, 6))
    x_data, y_data_fb, y_data_dc = [], [], []
    ln_fb, = plt.plot([], [], label='Força Bruta', marker='o', linestyle='-', color='blue')
    ln_dc, = plt.plot([], [], label='Divisão e Conquista', marker='s', linestyle='-', color='orange')

    def init():
        ax.set_xlim(min(n_values), max(n_values))
        ax.set_ylim(0, max(max(tempos_forca_bruta.values()), max(tempos_divisao_conquista.values())) * 1.1)
        ax.set_xlabel('Tamanho da Entrada (n)')
        ax.set_ylabel('Tempo Médio de Execução (s)')
        ax.set_title('Comparação de Algoritmos - Par de Pontos Mais Próximos')
        ax.legend()
        ax.grid()
        return ln_fb, ln_dc

    def update(frame):
        n = n_values[frame]
        x_data.append(n)
        y_data_fb.append(tempos_forca_bruta[n])
        y_data_dc.append(tempos_divisao_conquista[n])
        
        # Atualiza os dados das linhas
        ln_fb.set_data(x_data, y_data_fb)
        ln_dc.set_data(x_data, y_data_dc)
        
        return ln_fb, ln_dc

    ani = FuncAnimation(fig, update, frames=len(n_values), init_func=init, blit=True, interval=200, repeat=False)
    plt.show()

if __name__ == "__main__":
    # Gerar entre 100 e 200 valores de n aleatórios entre 10 e 10.000, em escala logarítmica
    k = random.randint(100, 200)
    n_values = sorted(set(map(int, np.logspace(1, 3.5, k))))

    # Escolher um valor de m aleatório entre 10 e 20
    m = random.randint(10, 20)

    # Comparar os algoritmos
    tempos_forca_bruta, tempos_divisao_conquista, diferencas_por_n = comparar_algoritmos(n_values, m)

    # Exibir diferenças encontradas
    for n, diferencas in diferencas_por_n.items():
        if diferencas > 0:
            print(f"Aviso: {diferencas} diferenças encontradas para n = {n}")

    # Criar animação do gráfico
    animar_grafico(n_values, tempos_forca_bruta, tempos_divisao_conquista)0