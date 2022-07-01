#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
lista = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3,1):
    for j in range(0,3,1):
        lista[i][j] = int(input('Digite um valor:'))
i = j =0
for i in range(0,3,1):
    for j in range(0,3,1):
        print('[{}]'.format(lista[i][j]), end=' ')
    print()