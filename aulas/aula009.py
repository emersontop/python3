frase = 'curso em video python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print("""eu to sem ideia de text
vou escrever qualquer coisa
eu do futo pfvr entenda""")

print(frase.count('o')) #conta quantos 'o' tem na string frase
print(frase.upper().count('O')) #upper transforma tudo par maiusculo
print(frase.upper())
print(len(frase)) #conta quantos locais de memoria ele ocupa
print(len(frase.strip())) #strip remove os espaços indesejados, no inicioe no final
print(frase.replace('python', 'android')) #troca o pyton por android, mas não altera a base para alterar temos que atribuir esse novo valor a frase
print('curso' in frase) #retonar um boleano
print(frase.split())