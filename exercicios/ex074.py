#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

#importando biblioteca random

import random as rd

#sortei da tupla de 5 numeros
tup = (rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10),rd.randint(1,10))
#print da tuplas
print(tup)
#print do maior numero
print(max(tup))
#print menor numero
print(min(tup))