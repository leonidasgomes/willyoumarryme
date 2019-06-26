'''
2019-06-26
Programa quer casar comigo
Desenvolvido por leonidasgomes
Visite meu guithub:leonidasgomes
Contribuindo com Amor :)
'''
#funcao que trata a resposta do casamento
def casar(resp):
resp=resp.upper()
if resp == 'S':

  print('S2')

elif resp == 'N':

  print('Bug')

else:
  respagain = input('Resposta invalida responda S para sim e N Para nao:')   
  
  casar(respagain)
  

# Variavel com a Pergunta Inicial 
pergunta='Voce quer casar comigo?'

# Exibindo a a pergunta
print(pergunta)

# Variavel que coleta a resposta
resposta =input('S ou N?')

# Chamando a função que trata a pergunta
casar(resposta)