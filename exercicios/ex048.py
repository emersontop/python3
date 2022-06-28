# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for i in range(3,500,3):
    print(i, end =' ')
    soma = i + soma
print('O resultado da soma de todos os numeros multiplos de 3 e que estão entre 3 e 500 é: {}'.format(soma))
