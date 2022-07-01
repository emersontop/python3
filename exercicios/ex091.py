#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#iniciando o programa
print('inicio do programa: ')

#importando a biblioteca random:
import random
import time
import operator
print('Valores sorteados: ')
ranking = dict()
res =  {'jogador 1':random.randint(1,6), 
        'jogador 2':random.randint(1,6),
        'jogador 3':random.randint(1,6),
        'jogador 4':random.randint(1,6),
        'jogador 5':random.randint(1,6),
        'jogador 1':random.randint(1,6)}
for v,k in res.items():
    print('o {} tirou o dado: {}'.format(v,k))
    time.sleep(1)
print('{}'.format('-='*20))

ranking = sorted(res.items(), key = operator.itemgetter(1), reverse=True)
for v,k in enumerate(ranking):
    print('o {} colocado foi {} com o valor de {}'.format(v+1,k[0],k[1]))
    time.sleep(1)
