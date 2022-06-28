#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
#Laço de repetição para entrada de dados
for i in range(0,6,1):
    #num recebe o dado digitado pelo usuário
    num = int(input('Digite um numero inteiro: '))
    #Aqui ele faz a validação se num é par, pelo resto da divisão.
    if num%2 == 0:
        soma = soma + num

print('A soma dos umeros pares é: {}'.format(soma))

##pulei para aula 14