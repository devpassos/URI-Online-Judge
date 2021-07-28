'''
Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários triângulos,
numa cartolina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos
com três varetas de comprimentos quaisquer: se uma das varetas for muito grande em relação às outras duas,
não dá para formar o triângulo.

Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas,
é ou não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.

Entrada
A entrada é composta por apenas uma linha contendo quatro números inteiros A, B, C e D (1 ≤ A, B, C, D ≤ 100).

Saída
Seu programa deve produzir apenas uma linha contendo apenas um caractere, que deve ser ‘S’ caso seja possível formar
o triângulo, ou ‘N’ caso não seja possível formar o triângulo.

'''

# Pega a entrada do usuário, quebra em um array mapeando-as como ponto flutuante.
entrada = list(map(float, input().split()))

# Atribui às variáveis cada um dos valores contidos no array de entrada.
a, b, c, d = entrada[0], entrada[1], entrada[2], entrada[3]

# Verifica se os valores passados formam um triângulo
if (1 <= a <= 100) and (1 <= b <= 100) and (1 <= c <= 100) and (1 <= d <= 100):
    if ((abs(b - c) < a < b + c) and
            (abs(a - c) < b < a + c) and
            (abs(a - b) < c < a + b)

            or ((abs(b - d) < a < b + d) and
                (abs(a - d) < b < a + d) and
                (abs(a - b) < d < a + b))

            or ((abs(c - d) < a < c + d) and
                (abs(a - d) < c < a + d) and
                (abs(a - c) < d < a + c))

            or ((abs(c - d) < b < c + d) and
                (abs(b - d) < c < b + d) and
                (abs(b - c) < d < b + c))):

        print('S')

    else:
        print('N')

else:
    print('N')