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