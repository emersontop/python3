#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro: '))
print(''' Escolhas uma das bases para a conversão
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')

opcao = int(input('Sua opção: '))
if opcao ==1:
    print('O numero {} Convertido para Binário é {}!'.format(num, bin(num)))
elif opcao == 2:
    print('O numero {} Convertido para Octal é {}!'.format(num, oct(num)))
elif opcao == 3:
    print('O numero {} Convertido para Hexadecimal é {}!'.format(num, hex(num)))
    