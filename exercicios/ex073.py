#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

#criação da lista

lista = (1,4,5,7,8,9,55,2,3,6,12,14,15,19,17,21,35,78,0,4)

#Print dos 5 primeiros numeros nas posições 0,1,2,3,4
print(lista[:5])
#print ultimos 4 colocados em -1,-2,-3,-4
print(lista[-4:])
#print de maneira organizada, lembrar que não altera
print(sorted(lista))
#print de posição na lista
print(lista.index(55))