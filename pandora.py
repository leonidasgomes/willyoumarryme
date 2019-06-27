'''
2019-06-26
Programa quer casar comigo
Desenvolvido por leonidasgomes
Visite meu guithub:leonidasgomes
Contribuindo com Amor :)
'''
# requests

import urllib.request, urllib.parse, urllib.error
   
nome=''

#funcao que trata a resposta do casamento
def casar(respo):
    respagain=''
    respo = respo.upper()
    if respo == 'S':

        frase = 'Eu te Amo'+nome

        print('\n'.join([''.join([(frase[(x-y) % len(frase)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))
        
    elif respo == 'N':

        print('Bug')

    else:
        respagain = input('Resposta invalida responda S para sim e N Para nao:')   
  
        casar(respagain)
  

nome=input('Qual é o seu 1° nome?')


if nome == 'Ney':
     
    url = 'https://media.licdn.com/dms/image/C4E03AQF0uyemBeO9XA/profile-displayphoto-shrink_800_800/0?e=1567036800&v=beta&t=VrAX8YFWfcarhS_uXt-_rHm90vRIyp5vaEzq0sYqBh0'
 

    print("Baixando com sua foto")
    f = urllib.request.urlopen(url)
    data = f.read()
    with open("/img/img.jpg", "wb") as code:
        code.write(data)

    from PIL import Image
    im = Image.open("/img/img.jpg")
    imgplot = plt.imshow(im)

else:


# Variavel com a Pergunta Inicial 
pergunta='Voce quer casar comigo?'

# Exibindo a a pergunta
print(pergunta)

# Variavel que coleta a resposta
resposta =input('S ou N?')

# Chamando a função que trata a pergunta
casar(resposta)