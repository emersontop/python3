cidade = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(cidade.count('A')))
print('A primeira letra A aparece na posição {} '.format(cidade.find('A')+1))
print('A ultima letra A aparece na posição {} '.format(cidade.rfind('A')+1))