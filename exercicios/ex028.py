#
import random
n1 = int(input('Escolha um número inteiro entre 0 e 5: '))
if n1 > 5:
    print('Você digitou um numero invalido')
npc = random.randint(0,5)
if n1==npc:
    print('Paranbens você acertou!!')
else:
    print('Eita... Não foi foi dessa vez, o número do sorteado foi {}'.format(npc))