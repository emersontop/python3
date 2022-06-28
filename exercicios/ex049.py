#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um numero inteiro para ver sua taboada: '))
for i in range(0,11,1):
    print('{} x {} = {}'.format(num,i,i*num))
print('Acabou!')