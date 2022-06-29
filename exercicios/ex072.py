#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

#criando uma lista com os valores cursivos
cursivo = ('zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
#iniicnando a condição do loop while
i=1
while i!=0:
    #coletando o dado do usuário
    num = int(input('Digite um número entre zero e 10: '))
    #validando o dado:
    if num>10 or num<0:
        #mensagem de erro
        print('Você digitou um numero fora do range:')
    else:
        #condição de saida do loop while
        i=0
#print da respostas
print('O numero que você digitou é: {}'.format(cursivo[num]))
