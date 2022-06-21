#nome = input('Qual é o seu nome? ')
#print('Prazer, meu nome é {:>20}'.format(nome))
#O :>20 alinha na posição 20 o nome. Podemos alinhar a esquerda :<20 Podemos centralizar :^20. Podemos centralizar colocando iguais em volta :=^20
#se você quer trabalhar apenas com 2 casas decimais flutuantes :.3f
#se você não quiser quebrar a linha no print você pode coloca, end=''

n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor valor'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s,m,d), end='')
print('Divisão inteira {} e pontência{}'.format(di,e))