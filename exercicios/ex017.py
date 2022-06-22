#calculo de hipotenusa
import math
cat1 = float(input('Digite o valor do cateto adjacente: '))
cat2 = float(input('Digite o valor do cateto oposto: ')) 
#print('A hipotenusa vale: {}'.format((cat1**2 + cat2**2)**(1/2)))
print('A hipotenusa vale: {}'.format(math.hypot(cat1,cat2)))
#hypot é uma função da bulioteca math