#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

#inicio do programa
print('Vai começar a brincadeira!!!')

#Iniciando a lista oficial:
lista = []

#inicia o contador:
cont = 0

while True:
    #marca o contador
    cont = cont +1
    #iniciando a lista auxiliar:
    lista2 = ['nome',14]
    #armazena na primeira posição da lista o nome
    lista2[0] = str(input('Qual o seu nome? '))
    #armazena na segunda posição da lista o peso
    lista2[1] = int(input("Qual o seu peso? "))
    #adiciona os valores a lista oficial
    lista.append(lista2[:])
    #checa se deseja continuar:
    res = str(input("Deseja continuar? [S/N] ")).upper()
    #vailida se digitou certo
    while res!= 'N' and res!='S':
        print('Você digitou errado, digite novamente!')
        res = str(input("Deseja continuar a adicionar números? [S/N] ")).upper()
    if res == 'N':
        break


