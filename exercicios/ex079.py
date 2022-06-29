#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
#Inicio do programa:
print('Inicio do programa: ')

#Inicando a lista
lista = []

#inicio do loop
while True:
    #recebendo o input do usuário:
    num = (int(input('Pofavor digite um valor, esse valor será adicionado a lista: ')))
    #checando se ele esta na lista
    if num in lista:
        #se ele estiver não faça nada
        print('O numero ja esta na lista.')
    else:
        #se o numero não estiver adicione ele
        lista.append(num)
        print('Numero {} adicionadp'.format(num))
    cont = str(input("Deseja continuar a adicionar numeors? [S/N] ")).upper()
    while cont!= 'N' and cont!='S':
        print('Você digitou o numero errado, digite novamente!')
        cont = str(input("Deseja continuar a adicionar numeors? [S/N] ")).upper()
    if cont == 'N':
        break
lista.sort()
print(lista)
    