'''
Neste projeto, você deverá criar um programa que irá gerar um número dentro de uma faixa (ex: 1 a 100). Além disso o
programa deverá permitir que o usuário chute o valor até que ele acerte. Seu programa deverá dar dicas sobre quão
próximo o valor digitado foi ao valor que foi realmente gerado pelo seu programa. Finalmente o usuário deverá ser
oferecido a opção de jogar novamente, se quiser.
'''

import os
from funcoes import *
from rich import print


# ABERTURA
os.system('clear')
print('*'*33)
print('Seja bem vindo a brincadeira...')
print('*'*33)
print('Olá, sou o bot -[bold][green]L3UN4M3[/][/]- e irei jogar com você, tudo bem?')
print('O jogo consiste em você adivinhar o numero que estou pensando..'+'\n'+'Vamos jogar?')

input('Para continuar tecle < Enter > ')


# # APRESENTAR O RANGE DE NUMEROS

os.system('clear')
print('Escolhi um número entre 0 e 50 e você deve acertar qual foi!')



# SOLICITAR O CHUTE DE NUMERO E CASO ACERTO, PARABENIZAR

escolha()

# REPETIR
while True:
    repetir = input('Quer jogar novamente? ')
    if repetir not in ['s','n']:
        os.system('clear')
        print('Opção errada. Para jogar novamente digite')
        # repetir = input('Quer jogar novamente? ')
    if repetir == 's':
        os.system('clear')
        escolha()
        
# SAINDO DO JOGO

    elif repetir == 'n':
        sair()

