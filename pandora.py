'''
2019-06-26
Programa quer casar comigo
Desenvolvido por leonidasgomes
Visite meu guithub:leonidasgomes
Contribuindo com Amor :)
'''
# requests
nome=''
import os, time
os.system('cls')
amor =  ["text1.txt","text2.txt"]

def animator(filenames,delay, repeat):
    frames = []
    for name in filenames:
        with open(name, "r",encoding="utf8") as f:
            frames.append(f.readlines())
        for i in range(repeat):
            for frame in frames:
                print("".join(frame))
                time.sleep(delay)
                os.system('cls')        
            
   


#funcao que trata a resposta do casamento
def casar(respo):
    respagain=''
    respo = respo.upper()
    if respo == 'S':

        frase = 'Eu te Amo '+nome

        frase=frase.upper()

        print('\n'.join([''.join([(frase[(x-y) % len(frase)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))
        
              

    elif respo == 'N':

        print('Bug')

    else:
        respagain = input('Resposta invalida responda S para sim e N Para nao:')   
  
        casar(respagain)
  

nome=input('Qual é o seu 1° nome?')


if nome == 'Ney':
     
    animator(amor,delay = 0.4, repeat = 3)

    print("""
        4 anos no mesmo jardim de infancia... 
        6 anos na mesma faculdade... 
        18 vezes cruzando o mesmo caminho... 
        1 beijo negado... 
        1 canoa quebrada...  
        """)
    print("""
        1 segunda chance ... 
        2 provas ...  
        2 despedidas ... 
        25 km de distancia ...
        1 Nova Vida... 
        Infinitas possibilidades...     
        """)            

    # Variavel com a Pergunta Inicial 
    pergunta = 'Voce quer casar comigo?'

    # Exibindo a a pergunta
    print(pergunta)

    # Variavel que coleta a resposta
    resposta =input('S ou N?')

    # Chamando a funcão que trata a pergunta
    casar(resposta)
    
else:

    print('Ha essa mensagem não para voce Obrigado :)')

    

