# dados.py

# 1 - Conjunto de dados "normal" onde os três algoritmos se comportam de maneira similar.
a1 = [
    [7, 9, 3, 4, 8],
    [8, 5, 6, 4, 5]
]
t1 = [
    [2, 3, 1, 3],
    [2, 1, 2, 1]
]
e1 = [2, 4]
x1 = [3, 2]
desc1 = "Conjunto de dados normal, resultados devem ser semelhantes."


# 2 - Conjunto de dados onde a programação dinâmica deve gerar o pior tempo (esse cenário é mais difícil de forçar pois é otimizado).
# Tentaremos criar um caso onde a programação dinâmica vai ser "induzida" a seguir um caminho menos vantajoso.
a2 = [
    [100, 1, 100, 1, 100],
    [1, 100, 1, 100, 1]
]
t2 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]
e2 = [100, 1] # Fazer a linha 1 ter uma entrada muito custosa
x2 = [1, 1] # Fazer a linha 2 ter uma saida muito curta, assim induzir o algoritmo a ir para linha 2
desc2 = "Programação dinâmica deve gerar o pior tempo."



# 3 - Conjunto de dados onde o algoritmo guloso deve gerar o pior tempo.
a3 = [
    [100, 1, 100, 1, 100, 1, 100, 1],
    [1, 100, 1, 100, 1, 100, 1, 100]
]
t3 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]
e3 = [1, 1]
x3 = [1, 1]
desc3 = "Algoritmo guloso deve gerar o pior tempo."


# 4 - Conjunto de dados onde a força bruta deve gerar o pior tempo (Na verdade, a força bruta sempre deve gerar o melhor tempo, a ideia é criar um cenario onde o tempo de computação seja muito alto).
# Em geral, a força bruta é sempre a melhor opção, mas pode levar muito tempo para dar a resposta. Esse valor gerará um tempo de computação alto.
a4 = [
    [10, 2, 10, 2, 10, 2, 10, 2, 10, 2, 10, 2],
    [2, 10, 2, 10, 2, 10, 2, 10, 2, 10, 2, 10]
]
t4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
e4 = [1, 1]
x4 = [1, 1]
desc4 = "Força bruta deve demorar muito para executar."


# 5 - Conjunto de dados com valores fracionados.
a5 = [
    [4, 5, 3, 2],
    [2, 10, 1, 4]
]
t5 = [
    [0.7, 0.6, 1.2],
    [1, 0.9, 0.5]
]
e5 = [1, 2]
x5 = [2, 1]
desc5 = "Conjunto de dados com valores fracionados."


# Para selecionar qual conjunto usar
conjunto_atual = 2 # Altere para 1, 2, 3, 4 ou 5 para usar um dos conjuntos acima


def get_dados():
    global conjunto_atual
    if conjunto_atual == 1:
        return a1, t1, e1, x1, desc1
    elif conjunto_atual == 2:
        return a2, t2, e2, x2, desc2
    elif conjunto_atual == 3:
        return a3, t3, e3, x3, desc3
    elif conjunto_atual == 4:
        return a4, t4, e4, x4, desc4
    elif conjunto_atual == 5:
        return a5, t5, e5, x5, desc5
    else:
        raise ValueError("Conjunto inválido. Use 1, 2, 3, 4 ou 5")


if __name__ == "__main__":
  a,t,e,x, desc = get_dados()
  print(f"conjunto atual: {conjunto_atual}")
  print("Dados para a linha de montagem:")
  print("a =", a)
  print("t =", t)
  print("e =", e)
  print("x =", x)
  print("descricao =", desc)