#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
i = 1
while i!=0:
    sexo = str(input('Digite o seu sexot [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        print('Seu sexo é top!')
        i=0

