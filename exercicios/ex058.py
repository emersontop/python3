#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

#importando a bilioteca

import random

#Iniciar a variável que será o contador de rodadas
cont=0

#condição de quebra de loop
i=1
while i!=0:
    numpc = random.randint(0,10)
    num=int(input('Escolhi meu numero entre 0 e 10, tente adivinha-lo: '))
    cont = cont +1
    if numpc == num:
        print('Parabens, você acertou! O numero que eu escolhi foi: {} Você tentou {} vezes'.format(numpc,cont))
        i=0
    else:
        print('Tente outra vez!')