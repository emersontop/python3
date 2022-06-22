d1 = float(input('Digite a distância da sua viagem: '))
if d1<= 200:
    valor = d1*0.5
else:
    valor = d1*0.45

print('O valor da viagem é de: {}'.format(valor))