n1 = input('digite um valor: ')
print(type(n1))
#Esse tipo vem em formato str, string, pq é o padrão se quisermos que venha formatado de algum modo coloque:
n1 = int(input('digite um valor: '))
print(type(n1))

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
nsoma = n1 + n2
print('O valor da soma entre {} e {} é:{}'.format(n1,n2,nsoma))

#Podemos usar o .isnumeric() pque retorna se a variável é numérica e podemos usar o .isalpha() para saber ser é alfabeto

print(nsoma.isnume)