# linha_montagem.py
from dados import get_dados, conjunto_atual
import sys

def linha_de_montagem_dinamica(a, t, e, x):
    """
    Encontra o menor tempo para montar um produto em duas linhas de montagem usando programação dinâmica.
    Retorna o menor tempo em minutos.
    """
    n = len(a[0])
    f1 = [0] * n
    f2 = [0] * n
    f1[0] = e[0] + a[0][0]
    f2[0] = e[1] + a[1][0]
    for j in range(1, n):
        f1[j] = min(f1[j - 1] + a[0][j], f2[j - 1] + t[1][j - 1] + a[0][j])
        f2[j] = min(f2[j - 1] + a[1][j], f1[j - 1] + t[0][j - 1] + a[1][j])
    menor_tempo = min(f1[n - 1] + x[0], f2[n - 1] + x[1])
    return menor_tempo, "O(n)" # Retorna o tempo e a analise assintotica

def linha_montagem_guloso(a, t, e, x):
    """
    Encontra o menor tempo para montar um produto em duas linhas de montagem usando um algoritmo guloso.
    Retorna o tempo em minutos.
    """
    n = len(a[0])
    tempo_total = 0
    linha_atual = 1 if e[0] <= e[1] else 2
    tempo_total += e[linha_atual - 1]

    for j in range(n):
        tempo_total += a[linha_atual - 1][j]
        if j < n - 1:
            tempo_linha_atual = tempo_total + a[linha_atual - 1][j+1]
            tempo_outra_linha = tempo_total + (t[linha_atual - 1][j] if linha_atual == 1 else t[linha_atual - 2][j]) + (a[2-linha_atual][j+1] if linha_atual == 1 else a[0][j+1])
            if tempo_outra_linha < tempo_linha_atual:
                linha_atual = 3 - linha_atual
    tempo_total += x[linha_atual - 1]
    return tempo_total, "O(n)" # Retorna o tempo e a analise assintotica

def linha_montagem_forca_bruta(a, t, e, x, j, linha_atual, tempo_atual):
    n = len(a[0])
    if j == n:
        return tempo_atual + x[linha_atual - 1]
    tempo_opcao1 = linha_montagem_forca_bruta(a, t, e, x, j + 1, linha_atual, tempo_atual + a[linha_atual - 1][j])
    tempo_opcao2 = sys.maxsize
    if j < n-1:
      outra_linha = 3 - linha_atual
      tempo_opcao2 = linha_montagem_forca_bruta(a, t, e, x, j + 1, outra_linha,
          tempo_atual + a[linha_atual - 1][j] + (t[linha_atual - 1][j] if linha_atual == 1 else t[linha_atual-2][j]))
    return min(tempo_opcao1, tempo_opcao2)

def inicializa_forca_bruta(a, t, e, x):
    menor_tempo1 = linha_montagem_forca_bruta(a, t, e, x, 0, 1, e[0])
    menor_tempo2 = linha_montagem_forca_bruta(a, t, e, x, 0, 2, e[1])
    return min(menor_tempo1, menor_tempo2), "O(2^n)" # Retorna o tempo e a analise assintotica

if __name__ == "__main__":
    a, t, e, x, desc = get_dados()

    print(f"Conjunto atual: {conjunto_atual}")
    print(desc)

    tempo_dinamica, analise_dinamica = linha_de_montagem_dinamica(a, t, e, x)
    print(f"Programação Dinâmica - Menor tempo: {tempo_dinamica:.2f} minutos, Análise Assintótica: {analise_dinamica}")

    tempo_guloso, analise_guloso = linha_montagem_guloso(a, t, e, x)
    print(f"Guloso --------------- Menor tempo: {tempo_guloso:.2f} minutos, Análise Assintótica: {analise_guloso}")

    tempo_forca_bruta, analise_forca_bruta = inicializa_forca_bruta(a, t, e, x)
    print(f"Força Bruta ---------- Menor tempo: {tempo_forca_bruta:.2f} minutos, Análise Assintótica: {analise_forca_bruta}")