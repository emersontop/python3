#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

#criação da condição de saida

i=1

#pegando os primeiros valores
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

#inicio do loop
while i!=0:
    opc=int(input(''' Escolha um das opções a baixo:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa'''))
    #Condição de valor invalido
    if opc>5 or opc<1:
        print('Opção invalida, digite novamente!')
    #condição [1] Soma
    if opc ==1:
        saida = num1+num2
        print('O valor da soma é: {}'.format(saida))
    #condição [2] Multiplicar
    if opc ==2:
        saida = num1*num2
        print('O valor da multiplicação é: {}'.format(saida))
    #condição [3] maior
    if opc ==3:
        if num1>num2:
            saida = num1
        if num2>num1:
            saida = num2
        if num1==num2:
            saida = num1
        print('O maior valor é: {}'.format(saida))
    #condição [4] novos numeros
    if opc ==4:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
    #condição [5] saia do programa
    if opc ==5:
        i=0