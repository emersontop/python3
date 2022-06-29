#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

#iniciando o programa:
print('Programa que lé e quarda 5 digitos, mostra o maior e o menor valor digitados e suas respectivas posições.')
#Iniciando a lista, posso inicar com ela recebendo list() ou com ela recebendo []
#lista = list()
lista = []
#iniciando o loop
for i in range(0,5,1):
    lista.append(int(input('Digite um valor inteiro na posição {} '.format(i))))
print('O maior valor é {} e ele esta na posição {}'.format(max(lista),lista.index(max(lista))))
print('O menor valor é {} e ele esta na posição {}'.format(min(lista),lista.index(min(lista))))