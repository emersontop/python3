#calculo de senos, cossenos e tangente
import math
a = float(input('Digite um angulo: '))
r = float(math.radians(a))
print('Para o angulo {} o valor do seno é: {} cosseno é: {} e tangente é {}'.format(r,math.sin(r),math.cos(r),math.tan(r)))