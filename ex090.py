#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dados = {}

dados['nome'] = str(input('Digite seu nome: '))
dados['nota'] = int(input('Digite sua nota {} : '.format(dados['nome'])))
if dados['nota']>=7:
    dados['situação']='Aprovado'
elif dados['nota']>=7 and dados['nota']<5:
    dados['situação']='Recuperação'
else:
    dados['situação']='Reprovado'

print(dados)

for k,v in dados.items():
    print('  - {} é igual a {}'.format(k,v))