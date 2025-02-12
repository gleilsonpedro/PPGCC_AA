import random
import time
import numpy as np
import matplotlib.pyplot as plt
from forca_bruta import par_mais_proximo_forca_bruta
from divisao_conquista import par_mais_proximo_divisao_conquista

def gerar_pontos(n):
    """Gera um conjunto de n pontos 2D aleatórios com coordenadas entre -2n e 2n."""
    limite = 2 * n
    return [(random.randint(-limite, limite), random.randint(-limite, limite)) for _ in range(n)]

# Gerar entre 100 e 200 valores de n aleatórios entre 10 e 10.000, igualmente espaçados
k = random.randint(100, 200)

###### atenção para a implementação do n_values, eu prefiro o com escala logaritmica, pela eficiência na distribuição achei melhor.

#n_values = sorted(random.sample(range(10, 1001), k)) #se quiser que termine no mesmo dia não coloque 10.000

n_values = sorted(set(map(int, np.logspace(1, 3.5, k))))  # Log scale evita muitos valores 

# grandes, neste caso a 
#distribuição dos valores é melhor evitando muitos valores grandes como pode acontecer com o random.sample(range(10, 3001)

# Escolher um valor de m aleatório entre 10 e 20
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
        p1_fb, p2_fb, dist_fb = par_mais_proximo_forca_bruta(pontos)
        fim = time.time()
        total_tempo_fb += (fim - inicio)
        
        # Executa Divisão e Conquista
        inicio = time.time()
        p1_dc, p2_dc, dist_dc = par_mais_proximo_divisao_conquista(pontos)
        fim = time.time()
        total_tempo_dc += (fim - inicio)
        
        # Verifica se os resultados são diferentes
        #if abs(dist_fb - dist_dc) > 1e-6:
        #    diferencas += 1
                # Verifica se os resultados são diferentes
        if abs(dist_fb - dist_dc) > 1e-6: # 1e-6 = 1x10
            diferencas += 1
            print(f"n = {n}, Diferença detectada!")
            print(f"  - Força Bruta: {dist_fb:.10f}")
            print(f"  - Divisão e Conquista: {dist_dc:.10f}")

    # Armazena os tempos médios
    tempos_forca_bruta[n] = total_tempo_fb / m
    tempos_divisao_conquista[n] = total_tempo_dc / m
    
    # Exibir avisos de diferenças nos resultados
    if diferencas > 0:
        print(f"Aviso: {diferencas} diferenças encontradas para n = {n}")

# Plotar gráfico
plt.figure(figsize=(10, 6))
plt.plot(n_values, list(tempos_forca_bruta.values()), label='Força Bruta', marker='o')
plt.plot(n_values, list(tempos_divisao_conquista.values()), label='Divisão e Conquista', marker='s')
plt.xlabel('Tamanho da Entrada (n)')
plt.ylabel('Tempo Médio de Execução (s)')
plt.title('Comparação de Algoritmos - Par de Pontos Mais Próximos')
plt.legend()
plt.grid()
plt.show()