cidade = str(input('Em qual cidade você nasceu: '))
cidade = str(cidade.strip())
cidade = str(cidade.lower())
cidade = cidade.split()
print('santo' in cidade[0])