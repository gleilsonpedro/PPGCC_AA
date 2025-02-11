import math
import random
from forca_bruta import par_mais_proximo_forca_bruta

def distancia_euclidiana(p1, p2):
    """Calcula a distância euclidiana entre dois pontos p1 e p2."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def par_mais_proximo_divisao_conquista(pontos):
    """Encontra o par de pontos mais próximo usando divisão e conquista."""
    def closest_pair_rec(px, py):
        if len(px) <= 3:
            return par_mais_proximo_forca_bruta(px)  # Chama a função corretamente

        mid = len(px) // 2
        mid_point = px[mid]

        Qx, Rx = px[:mid], px[mid:]
        Qy = list(filter(lambda p: p[0] <= mid_point[0], py))
        Ry = list(filter(lambda p: p[0] > mid_point[0], py))

        p1_q, p2_q, dist_q = closest_pair_rec(Qx, Qy)
        p1_r, p2_r, dist_r = closest_pair_rec(Rx, Ry)

        if dist_q < dist_r:
            d, min_pair = dist_q, (p1_q, p2_q)
        else:
            d, min_pair = dist_r, (p1_r, p2_r)

        strip = [p for p in py if abs(p[0] - mid_point[0]) < d]

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                p, q = strip[i], strip[j]
                dist = distancia_euclidiana(p, q)
                if dist < d:
                    d, min_pair = dist, (p, q)

        return min_pair[0], min_pair[1], d

    px = sorted(pontos, key=lambda p: p[0])
    py = sorted(pontos, key=lambda p: p[1])
    return closest_pair_rec(px, py)

# Bloco de teste para rodar sozinho
if __name__ == "__main__":
    def gerar_pontos(n):
        """Gera um conjunto de n pontos 2D aleatórios com coordenadas entre -2n e 2n."""
        limite = 2 * n
        return [(random.randint(-limite, limite), random.randint(-limite, limite)) for _ in range(n)]

    # Teste rápido com n = 10
    pontos = gerar_pontos(10)
    p1, p2, distancia = par_mais_proximo_divisao_conquista(pontos)

    print(f"Par mais próximo: {p1} e {p2} com distância {distancia:.4f}")
