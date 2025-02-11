import math

def distancia_euclidiana(p1, p2):
    """Calcula a distância euclidiana entre dois pontos p1 e p2."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def par_mais_proximo_forca_bruta(pontos):
    """Encontra o par de pontos mais próximo usando força bruta."""
    n = len(pontos)
    menor_distancia = float('inf')
    p1, p2 = None, None

    for i in range(n):
        for j in range(i + 1, n):
            dist = distancia_euclidiana(pontos[i], pontos[j])
            if dist < menor_distancia:
                menor_distancia = dist
                p1, p2 = pontos[i], pontos[j]

    return p1, p2, menor_distancia

if __name__ == "__main__":
    import random

    def gerar_pontos(n):
        """Gera um conjunto de n pontos 2D aleatórios com coordenadas entre -2n e 2n."""
        limite = 2 * n
        return [(random.randint(-limite, limite), random.randint(-limite, limite)) for _ in range(n)]

    # Teste rápido com n = 10
    pontos = gerar_pontos(10)
    p1, p2, distancia = par_mais_proximo_forca_bruta(pontos)

    print(f"Par mais próximo: {p1} e {p2} com distância {distancia:.4f}")

