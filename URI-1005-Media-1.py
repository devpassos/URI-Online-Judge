#######################################################################################################
'''
Leia 2 valores de ponto flutuante de dupla precisão A e B,
que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno,
sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11).
Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal
e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e
como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário,
você receberá "Presentation Error".
'''
#######################################################################################################

# Inicia um Array vazio para guardar as notas
notas = []

# Cria um laço para pegar as entradas do usuário e guarda no array
# são solicitadas do usuário apenas duas entradas. Para a cada uma,
# já é feito o cáclulo do peso e quanto ele representa da média.
while (len(notas) < 2):
    n = input()
    if (len(notas) == 0):
        notas.append(((float(n) * 3.5) / 11))
    else:
        notas.append(((float(n) * 7.5) / 11))

# Apenas imprime o valor somado do array de notas.
print('MEDIA = %.5f' % sum(notas))