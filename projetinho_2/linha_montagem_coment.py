import time
import matplotlib.pyplot as plt
from projetinho_2.dados_old import get_dados

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

    return min(f1[n - 1] + x[0], f2[n - 1] + x[1])


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
    algoritmo(a, t, e, x)
    return time.perf_counter() - inicio


if __name__ == "__main__":
    # Obtém os dados do conjunto selecionado
    a, t, e, x, desc = get_dados()
    
    # Exibe descrição do conjunto de dados
    print(desc)

    # Mede os tempos de execução para o conjunto atual
    tempo_dinamica = medir_tempo_execucao(linha_de_montagem_dinamica, a, t, e, x)
    print(f"Programação Dinâmica - Tempo: {tempo_dinamica:.6f} segundos")

    # Se o número de estações for pequeno, mede a força bruta (evita tempos excessivos)
    if len(a[0]) <= 12:
        tempo_forca_bruta = medir_tempo_execucao(inicializa_forca_bruta, a, t, e, x)
        print(f"Força Bruta --------- Tempo: {tempo_forca_bruta:.6f} segundos")
    else:
        tempo_forca_bruta = None
        print("Força Bruta ignorada para evitar tempos excessivos.")

    # Gerando gráfico comparativo
    tamanhos_n = list(range(1, 13))  # Testa de 1 a 12 estações
    tempos_dinamica = []
    tempos_forca_bruta = []

    for n in tamanhos_n:
        # Gera um conjunto de dados aleatório de tamanho n
        a_teste = [[3] * n, [2] * n]
        t_teste = [[1] * (n-1), [1] * (n-1)] if n > 1 else [[], []]
        e_teste = [2, 2]
        x_teste = [3, 2]

        # Mede tempos
        tempos_dinamica.append(medir_tempo_execucao(linha_de_montagem_dinamica, a_teste, t_teste, e_teste, x_teste))
        if n <= 12:
            tempos_forca_bruta.append(medir_tempo_execucao(inicializa_forca_bruta, a_teste, t_teste, e_teste, x_teste))
        else:
            tempos_forca_bruta.append(None)  # Evita tempos muito longos

    # Plotando o gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(tamanhos_n, tempos_dinamica, label="Programação Dinâmica (O(n))", marker='o', linestyle='--')
    if None not in tempos_forca_bruta:
        plt.plot(tamanhos_n, tempos_forca_bruta, label="Força Bruta (O(2^n))", marker='s', linestyle='--', color='r')

    plt.xlabel("Número de Estações (n)")
    plt.ylabel("Tempo de Execução (segundos)")
    plt.title("Comparação de Tempo: Programação Dinâmica vs Força Bruta")
    plt.legend()
    plt.grid()
    plt.show()
