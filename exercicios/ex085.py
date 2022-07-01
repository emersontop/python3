#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#iniciando o programa

print('Inicio do programa: ')

#inicia a lista
lista = [[],[]]

#inicia o loop que vai contar de 1 ate 7 de 1 em 1
for i in range(1,8,1):
    #n = a entrada
    n=int(input('Por favor, digite o {}º número: '.format(i)))
    #Analisa de n é par ou impar
    if n%2 ==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print('Os numerps parres são: {} e os impares são: {}'.format(lista[0],lista[1]))
