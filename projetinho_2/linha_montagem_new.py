import time
import matplotlib.pyplot as plt
from dados import get_dados
import numpy as np


def linha_de_montagem_dinamica(a, t, e, x):
    """Algoritmo de Programação Dinâmica para a linha de montagem."""
    n = len(a[0])
    f1 = [0] * n
    f2 = [0] * n
    f1[0] = e[0] + a[0][0]
    f2[0] = e[1] + a[1][0]

    for j in range(1, n):
        f1[j] = min(f1[j - 1] + a[0][j], f2[j - 1] + t[1][j - 1] + a[0][j])
        f2[j] = min(f2[j - 1] + a[1][j], f1[j - 1] + t[0][j - 1] + a[1][j])

    tempo_producao = min(f1[n - 1] + x[0], f2[n - 1] + x[1])
    return tempo_producao


def linha_montagem_forca_bruta(a, t, e, x, j, linha_atual, tempo_atual):
    """Algoritmo de Força Bruta para a linha de montagem."""
    n = len(a[0])
    if j == n:
        return tempo_atual + x[linha_atual - 1]

    tempo_opcao1 = linha_montagem_forca_bruta(a, t, e, x, j + 1, linha_atual, tempo_atual + a[linha_atual - 1][j])

    tempo_opcao2 = float('inf')
    if j < n - 1:
        outra_linha = 3 - linha_atual
        tempo_opcao2 = linha_montagem_forca_bruta(a, t, e, x, j + 1, outra_linha,
                                                 tempo_atual + a[linha_atual - 1][j] + t[linha_atual - 1][j])

    return min(tempo_opcao1, tempo_opcao2)


def inicializa_forca_bruta(a, t, e, x):
    """Inicializa a execução do algoritmo de Força Bruta."""
    menor_tempo1 = linha_montagem_forca_bruta(a, t, e, x, 0, 1, e[0])
    menor_tempo2 = linha_montagem_forca_bruta(a, t, e, x, 0, 2, e[1])
    return min(menor_tempo1, menor_tempo2)


def medir_tempo_execucao(algoritmo, a, t, e, x):
    """Mede o tempo de execução de um algoritmo."""
    inicio = time.perf_counter()
    resultado = algoritmo(a, t, e, x)
    return resultado, time.perf_counter() - inicio


if __name__ == "__main__":

    # Testar com 14 conjuntos de dados
    for conjunto_atual in range(1, 15):
        # Obtém os dados do conjunto selecionado
        a, t, e, x, desc = get_dados(conjunto_atual)

        # Exibe descrição do conjunto de dados
        print(f"\n--- Conjunto de dados {conjunto_atual} ---")
        print(desc)  # Imprime a descrição da base atual

        # Mede os tempos de execução e os tempos de produção para o conjunto atual
        tempo_producao_dinamica, tempo_execucao_dinamica = medir_tempo_execucao(linha_de_montagem_dinamica, a, t, e, x)
        print(
            f"Programação Dinâmica - Tempo de Produção: {tempo_producao_dinamica:.2f} minutos, Tempo de Execução: {tempo_execucao_dinamica:.6f} segundos")

        # Se o número de estações for pequeno, mede a força bruta (evita tempos excessivos)
        if len(a[0]) <= 12:
            tempo_producao_forca_bruta, tempo_execucao_forca_bruta = medir_tempo_execucao(inicializa_forca_bruta, a, t, e, x)
            print(
                f"Força Bruta ---------- Tempo de Produção: {tempo_producao_forca_bruta:.2f} minutos, Tempo de Execução: {tempo_execucao_forca_bruta:.6f} segundos")
        else:
            tempo_execucao_forca_bruta = None
            print("Força Bruta ignorada para evitar tempos excessivos.")

    # Gerando gráfico comparativo
    tamanhos_n = list(range(1, 13))  # Testa de 1 a 12 estações
    tempos_execucao_dinamica_grafico = []
    tempos_execucao_forca_bruta_grafico = []

    # Define o conjunto de dados para o gráfico
    conjunto_grafico = 3
    
    for n in tamanhos_n:
        # Obtém dados do conjunto para o gráfico (agora dentro do loop)
        a_teste, t_teste, e_teste, x_teste, desc_grafico = get_dados(conjunto_grafico)
        
        a_teste = [[3] * n, [2] * n]
        t_teste = [[1] * (n - 1), [1] * (n - 1)] if n > 1 else [[], []]
        e_teste = [2, 2]
        x_teste = [3, 2]

        # Mede tempos
        _, tempo_execucao_dinamica = medir_tempo_execucao(linha_de_montagem_dinamica, a_teste, t_teste, e_teste, x_teste)
        tempos_execucao_dinamica_grafico.append(tempo_execucao_dinamica)

        if n <= 12:
            _, tempo_execucao_forca_bruta = medir_tempo_execucao(inicializa_forca_bruta, a_teste, t_teste, e_teste, x_teste)
            tempos_execucao_forca_bruta_grafico.append(tempo_execucao_forca_bruta)
        else:
            tempos_execucao_forca_bruta_grafico.append(None)  # Evita tempos muito longos

    # Converte para numpy arrays para facilitar as operações
    tempos_execucao_dinamica_grafico = np.array(tempos_execucao_dinamica_grafico)
    if None not in tempos_execucao_forca_bruta_grafico:
        tempos_execucao_forca_bruta_grafico = np.array(tempos_execucao_forca_bruta_grafico)

    # Aplica a transformação para microssegundos (opcional, pode mudar para milissegundos)
    tempos_execucao_dinamica_grafico *= 1_000_000  # Transformar em microssegundos
    if None not in tempos_execucao_forca_bruta_grafico:
        tempos_execucao_forca_bruta_grafico *= 1_000_000

    # Plotando o gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(tamanhos_n, tempos_execucao_dinamica_grafico, label="Programação Dinâmica (O(n))", marker='o', linestyle='--')
    if None not in tempos_execucao_forca_bruta_grafico:
        plt.plot(tamanhos_n, tempos_execucao_forca_bruta_grafico, label="Força Bruta (O(2^n))", marker='s', linestyle='--',
                 color='r')

    plt.xlabel("Número de Estações (n)")
    plt.ylabel("Tempo de Execução (µs)")  # Modificando rótulo
    plt.title(f"Comparação de Tempo:\nProgramação Dinâmica vs Força Bruta\n(Base de Dados: {conjunto_grafico} - {desc_grafico})")  # Modifiquei o titulo para mostrar os resultados corretos
    plt.yscale('log')  # Adicionando escala logarítmica
    plt.legend()
    plt.grid()
    plt.show()