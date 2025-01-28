import random
import math
import time

def gerar_pontos(n):
    """Gera um conjunto de n pontos 2D aleatórios com coordenadas entre -2n e 2n."""
    limite = 2 * n
    return [(random.randint(-limite, limite), random.randint(-limite, limite)) for _ in range(n)]

def distancia_euclidiana(p1, p2):
    """Calcula a distância euclidiana entre dois pontos p1 e p2."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

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

    return par_mais_proximo, menor_distancia

# Teste do algoritmo
if __name__ == "__main__":
    tamanhos = [10, 100, 500, 1000]  # Exemplos de tamanhos de entrada para testar
    resultados = {}

    for n in tamanhos:
        pontos = gerar_pontos(n)
        inicio = time.time()
        par, distancia = par_mais_proximo_forca_bruta(pontos)
        fim = time.time()

        resultados[n] = {
            "tempo": fim - inicio,
            "par": par,
            "distancia": distancia
        }

        print(f"Tamanho: {n}")
        print(f"Tempo de execução: {fim - inicio:.4f} segundos")
        print(f"Par mais próximo: {par} com distância {distancia:.4f}\n")
