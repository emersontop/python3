l1 = float(input('Digite o valor do lado 1: '))
l2 = float(input('Digite o valor do lado 2: '))
l3 = float(input('Digite o valor do lado 3: '))
maior= l1
if maior<= l2:
    maior = l2
if maior<= l3:
    maior = l3
menor = l1
if menor>= l2:
    menor = l2
if menor>= l3:
    menor = l3
if l1< maior and l1> menor:
    medio = l1
if l2< maior and l2> menor:
    medio = l2
if l3< maior and l3> menor:
    medio = l3
print('O lado maior É {} o menor pe {} o do meio é {}'.format(maior, menor, medio))
if maior >= medio +menor:
    print('Não pode ser triangulo')
else:
    print('é triangulo')
