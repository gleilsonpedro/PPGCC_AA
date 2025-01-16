import random
import math
import time
import matplotlib.pyplot as plt

def gerar_pontos(n):
    """Gera um conjunto de n pontos 2D aleatórios com coordenadas entre -2n e 2n."""
    limite = 2 * n
    return [(random.randint(-limite, limite), random.randint(-limite, limite)) for _ in range(n)]

def distancia_euclidiana(p1, p2):
    """Calcula a distância euclidiana entre dois pontos p1 e p2."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def par_mais_proximo_divisao_conquista(pontos):
    """Encontra o par de pontos mais próximo usando divisão e conquista."""
    def closest_pair_rec(px, py):
        # Base: menos de 3 pontos, use força bruta
        if len(px) <= 3:
            return par_mais_proximo_forca_bruta(px)

        # Divida o conjunto de pontos em duas metades
        mid = len(px) // 2
        mid_point = px[mid]

        Qx = px[:mid]
        Rx = px[mid:]

        Qy = list(filter(lambda p: p[0] <= mid_point[0], py))
        Ry = list(filter(lambda p: p[0] > mid_point[0], py))

        # Resolva recursivamente para cada metade
        (p1, q1, dist1) = closest_pair_rec(Qx, Qy)
        (p2, q2, dist2) = closest_pair_rec(Rx, Ry)

        # Determine a menor distância entre as duas metades
        if dist1 < dist2:
            d = dist1
            min_pair = (p1, q1)
        else:
            d = dist2
            min_pair = (p2, q2)

        # Verifique a faixa ao redor da linha divisória
        strip = [p for p in py if abs(p[0] - mid_point[0]) < d]

        # Verifique os pares na faixa
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                p, q = strip[i], strip[j]
                if p != q:  # Garantir que os pontos não sejam iguais
                    dist = distancia_euclidiana(p, q)
                    if dist < d:
                        d = dist
                        min_pair = (p, q)

        return min_pair[0], min_pair[1], d

    # Ordene os pontos por coordenada x e depois por coordenada y
    px = sorted(pontos, key=lambda p: p[0])
    py = sorted(pontos, key=lambda p: p[1])
    return closest_pair_rec(px, py)

def par_mais_proximo_forca_bruta(pontos):
    """Encontra o par de pontos mais próximo usando força bruta."""
    n = len(pontos)
    menor_distancia = float('inf')
    par_mais_proximo = None

    for i in range(n):
        for j in range(i + 1, n):
            dist = distancia_euclidiana(pontos[i], pontos[j])
            if dist < menor_distancia:
                menor_distancia = dist
                par_mais_proximo = (pontos[i], pontos[j])

    return par_mais_proximo[0], par_mais_proximo[1], menor_distancia

# Teste do algoritmo
if __name__ == "__main__":
    tamanhos = [10, 100, 500, 1000]  # Exemplos de tamanhos de entrada para testar
    resultados = {
        "forca_bruta": [],
        "divisao_conquista": []
    }

    for n in tamanhos:
        pontos = gerar_pontos(n)

        # Força bruta
        inicio = time.time()
        par1, par2, distancia1 = par_mais_proximo_forca_bruta(pontos)
        fim = time.time()
        tempo_forca_bruta = fim - inicio

        # Divisão e conquista
        inicio = time.time()
        par3, par4, distancia2 = par_mais_proximo_divisao_conquista(pontos)
        fim = time.time()
        tempo_divisao_conquista = fim - inicio

        resultados["forca_bruta"].append(tempo_forca_bruta)
        resultados["divisao_conquista"].append(tempo_divisao_conquista)

        print(f"Tamanho: {n}")
        print(f"Força Bruta: Tempo = {tempo_forca_bruta:.4f} s, Par = {par1} e {par2}, Distância = {distancia1:.4f}")
        print(f"Divisão e Conquista: Tempo = {tempo_divisao_conquista:.4f} s, Par = {par3} e {par4}, Distância = {distancia2:.4f}")
        print("-")

    # Plotar os gráficos
    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos, resultados["forca_bruta"], label="Força Bruta", marker="o")
    plt.plot(tamanhos, resultados["divisao_conquista"], label="Divisão e Conquista", marker="s")
    plt.xlabel("Tamanho da Entrada (n)")
    plt.ylabel("Tempo de Execução (s)")
    plt.title("Comparação de Tempo de Execução")
    plt.legend()
    plt.grid()
    plt.show()
