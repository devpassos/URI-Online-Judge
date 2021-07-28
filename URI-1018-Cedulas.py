'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser
decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação
de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a
mensagem: “Presentation Error”.
'''

# Pega a entrada do usuáro (um valor inteiro)
valor = int(input())

# Declara um array com os valores de das cédulas, que serão usados para dividir o valor passado na entrada.
cedulas = [100, 50,  20, 10, 5, 2, 1]

# Imprime o valor passado pelo usuário na tela.
print(valor)

# Laço que pega o valor pasado e faz uma divisão inteira por cada cédula. Subtrai o montante de cadas uma das cédulas
# do valor total até chegar à última.
# Para cada iteração imprime a quantidade de cédulas necessárias para formar o valor.
for x in cedulas:
    cedula_temp = valor // x
    valor_formatado = '%d nota(s) de R$ %.2f' % (cedula_temp, x)
    print(valor_formatado.replace('.', ','))
    valor -= (cedula_temp * x)








