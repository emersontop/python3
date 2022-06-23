#Exercício Python 036: 
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
#o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. 

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Quantos ano você deseja terminar de pagar? '))

#Calculo da prestação mensal.

presta = casa/(anos*12) 

#verificação da condição de aprovação

if presta <= (0.3*salario):
    print('Parabens você pode comprar a casa no valor de R${} pagando prestações mensais de R${}'.format(casa,presta))
else:
    print('Você não tem condições para comprar a casa')