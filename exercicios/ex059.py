#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um numero: '))
print('O fatorial de {} é'.format(num,num),end = ' ')
fat= 1
while num!=0:
    print('{}'.format(num),end =' ')
    fat = fat*num
    num = num -1
print(' = {}'.format(fat))