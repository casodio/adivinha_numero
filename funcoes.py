from random import choice, randrange 
import os
from time import sleep



def escolha():
    mente_bot = randrange(0,51)
    opcao = int(input('Qual número será que eu estou pensando? '))
    
    while opcao != mente_bot:

        if opcao < mente_bot:
            os.system('clear')
            print(choice(maior))
            opcao = int(input('Qual número será que eu estou pensando? '))

        elif opcao > mente_bot:
            os.system('clear')
            print(choice(menor))
            opcao = int(input('Qual número será que eu estou pensando? '))

    if opcao == mente_bot:
        print(choice(acertou))

def sair():
    print('*'*70)
    print('Obrigado por jogar com comigo. Quer ver mais? segue nosso GitHub:')
    print('[green]https://github.com/casodio','\n')
    print('*'*70)
    sleep(3)
    exit()

acertou = ['Você acertou :) Parabens!!', 'Boa, você é espetacular!', 'Isso... Parabens.', 'Acertou, você é demais mesmo.', 'Nossa, você é demais.']
maior = ['Um pouco mais...', 'Um numero maior', 'Quase, um maior..', 'Ta quente, aumenta mais', 'Essa foi quase, mas ele é um pouco maior.']
menor = ['Nossa, você quase acertou.. Mas é um numero menor', 'Ta quase mas ainda não foi. Diminui mais um pouco! ',
 'Calma que vai, um pouco menos.','Vai dar certo. é menor que esse ultimo.','Caramba, quase foi. Diminui mais...']
