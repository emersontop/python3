v1 = float(input('Qual a velocidade do seu carro? '))
if v1 > 80:
    print('Você passou do limite de velocidade! Você foi multado!')
    multa = (v1 - 80) * 7
    print('O valor da multa é {}'.format(multa))
else:
    print('Tudo bem! Boca viagem!')