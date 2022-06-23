#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
ano = int(input('Digite o ano que vocÊ nasceu: '))
idade = (datetime.date.today().year)-ano
print('Você tem {} anos.'.format(idade))

if idade > 18:
    print('Você esta atrasado {} anos.'.format(idade-18))
elif idade == 18:
    print('Esse é seu ano de alistamento!')
elif idade < 18:
    print('Ainda faltam {} anos para você se alistar.'.format(18-idade))