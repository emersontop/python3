n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite outro numero:'))
if n1> n2 and n1>n3:
    print('{} É o maior numero!'.format(n1))
if n2> n1 and n2>n3:
    print('{} É o maior numero!'.format(n2))
if n3> n1 and n3>n2:
    print('{} É o maior numero!'.format(n3))
if n1< n2 and n1<n3:
    print('{} É o menor numero!'.format(n1))
if n2< n1 and n2<n3:
    print('{} É o menor numero!'.format(n2))
if n3< n1 and n3<n2:
    print('{} É o menor numero!'.format(n3))