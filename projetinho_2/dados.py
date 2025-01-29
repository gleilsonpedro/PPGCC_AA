# dados.py
# a = tempo de produção na estação
# t = tempo entre as estações
# e = tempo de entradas
# x = tempo de saída

import random

# 1 - Conjunto de dados "normal" onde os três algoritmos se comportam de maneira similar.
a1 = [
    [7, 9, 3, 4, 8, 4],
    [8, 5, 6, 4, 5, 7]
]
t1 = [
    [2, 3, 1, 3, 4],
    [2, 1, 2, 2, 1]
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
desc2 = "Programação dinâmica deve ser induzida a um caminho pior."


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
desc3 = "Conjunto com alta variação para testar diferentes caminhos."


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

# 6 - Conjunto de dados com valores grandes
a6 = [
    [50, 80, 120, 60, 150],
    [70, 40, 100, 90, 130]
]
t6 = [
    [10, 5, 15, 8],
    [12, 7, 9, 11]
]
e6 = [30, 20]
x6 = [15, 25]
desc6 = "Conjunto de dados com valores grandes."

# 7 - Conjunto de dados com trocas de linhas frequentes
a7 = [
    [5, 100, 5, 100, 5, 100],
    [100, 5, 100, 5, 100, 5]
]
t7 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]
e7 = [2, 2]
x7 = [1, 1]
desc7 = "Conjunto de dados com trocas de linhas frequentes."

# 8 - Conjunto de dados com um linha mais rápida que outra
a8 = [
    [10, 10, 10, 10, 10],
    [2, 2, 2, 2, 2]
]
t8 = [
    [1, 1, 1, 1],
    [10, 10, 10, 10]
]
e8 = [1, 1]
x8 = [1, 1]
desc8 = "Conjunto de dados com uma linha mais rápida que outra."

# 9 - Conjunto de dados com muita variação entre estações
a9 = [
    [1, 100, 10, 1000, 1],
    [1000, 1, 100, 10, 1000]
]
t9 = [
    [5, 2, 8, 1],
    [3, 7, 1, 9]
]
e9 = [5, 1]
x9 = [1, 5]
desc9 = "Conjunto de dados com alta variação entre estações."

# 10 - Conjunto de dados com penalidades de transição altas
a10 = [
    [5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5]
]
t10 = [
    [20, 25, 30, 35],
    [35, 30, 25, 20]
]
e10 = [1, 1]
x10 = [1, 1]
desc10 = "Conjunto de dados com penalidades de transição altas."


# 11 - Conjunto de dados que força a troca de linha no final
a11 = [
    [5, 5, 5, 5, 100],
    [5, 5, 5, 5, 1]
]
t11 = [
  [1, 1, 1, 1],
  [1, 1, 1, 1]
]
e11 = [1, 1]
x11 = [100, 1]
desc11 = "Conjunto que força a troca de linha no final."


# 12 - Conjunto de dados com muitas estações e valores variados
a12 = [
    [2, 5, 1, 8, 3, 9, 4, 6, 2, 7],
    [7, 2, 6, 4, 9, 3, 8, 1, 5, 2]
]
t12 = [
    [3, 6, 2, 5, 1, 4, 7, 2, 8],
    [1, 4, 3, 7, 2, 5, 1, 6, 3]
]
e12 = [2, 1]
x12 = [3, 2]
desc12 = "Conjunto com muitas estações e valores variados."

# 13 - Conjunto de dados aleatório
def gerar_dados_aleatorios(n):
    a = [
        [random.randint(1, 100) for _ in range(n)],
        [random.randint(1, 100) for _ in range(n)]
    ]
    t = [
        [random.randint(1, 10) for _ in range(n - 1)] if n > 1 else [],
        [random.randint(1, 10) for _ in range(n - 1)] if n > 1 else []
    ]
    e = [random.randint(1, 100), random.randint(1, 100)]
    x = [random.randint(1, 100), random.randint(1, 100)]
    return a, t, e, x

a13, t13, e13, x13 = gerar_dados_aleatorios(random.randint(5, 15))
desc13 = "Conjunto de dados totalmente aleatório."

# 14 - Conjunto de dados com mais estações
def gerar_dados_estacoes(n):
  a = [
      [random.randint(1, 100) for _ in range(n)],
      [random.randint(1, 100) for _ in range(n)]
  ]
  t = [
      [random.randint(1, 10) for _ in range(n-1)] if n > 1 else [],
      [random.randint(1,10) for _ in range(n-1)] if n > 1 else []
  ]
  e = [random.randint(1,100), random.randint(1,100)]
  x = [random.randint(1, 100), random.randint(1, 100)]
  return a,t,e,x

a14, t14, e14, x14 = gerar_dados_estacoes(random.randint(20,30))
desc14 = "Conjunto de dados com mais estações."

# Para selecionar qual conjunto usar
conjunto_atual = 12  # Altere para um valor de 1 a 14 para selecionar um conjunto específico.


def get_dados(conjunto_atual):
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
    elif conjunto_atual == 6:
        return a6, t6, e6, x6, desc6
    elif conjunto_atual == 7:
        return a7, t7, e7, x7, desc7
    elif conjunto_atual == 8:
      return a8, t8, e8, x8, desc8
    elif conjunto_atual == 9:
      return a9, t9, e9, x9, desc9
    elif conjunto_atual == 10:
      return a10, t10, e10, x10, desc10
    elif conjunto_atual == 11:
      return a11, t11, e11, x11, desc11
    elif conjunto_atual == 12:
      return a12, t12, e12, x12, desc12
    elif conjunto_atual == 13:
      return a13, t13, e13, x13, desc13
    elif conjunto_atual == 14:
      return a14, t14, e14, x14, desc14
    else:
        raise ValueError("Conjunto inválido. Use um valor de 1 a 14")


if __name__ == "__main__":
  a,t,e,x, desc = get_dados(1)
  print(f"conjunto atual: {conjunto_atual}")
  print("Dados para a linha de montagem:")
  print("a =", a)
  print("t =", t)
  print("e =", e)
  print("x =", x)
  print("descricao =", desc)