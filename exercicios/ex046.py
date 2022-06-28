import time
print('Contagem regressiva para o inicio dos fogos de artifício: ')
for i in range(10,-1,-1):
    print("Faltam {} segundos para o início".format(i))
    time.sleep(1)
print('Que comece a festa!')