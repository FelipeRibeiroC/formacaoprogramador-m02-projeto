# -*- coding: utf-8 -*-
"""MeuJogoParOuImpar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13wg-SKW-2qC8GGadMHs9BuRAeJq30D-F
"""

jogador1 = input('-> Digite o nome do primeiro jogador:')
jogador2 = input('-> Digite o nome do segundo jogador:')

print(f'// Quem escolhe primeiro, {jogador1} ou {jogador2}?')
primeiro_jogador = input(f'-> Digite 1 para escolher {jogador1} ou 2 para escolher {jogador2}.')
segundo_jogador = None

if primeiro_jogador == '1':
  primeiro_jogador = jogador1
  segundo_jogador = jogador2
elif primeiro_jogador == '2':
  primeiro_jogador = jogador2
  segundo_jogador = jogador1

print('// Digite 0 para escolher PAR ou 1 para escolher ÍMPAR')
escolha = input(f'-> {primeiro_jogador}, você quer par ou impar?')
escolha2 = None

if escolha == 'ímpar' or escolha == 'impar' or escolha == '1':
  escolha = 'ímpar'
  escolha2 = 'par'
elif escolha == 'par' or escolha == '0':
  escolha = 'par'
  escolha2 = 'ímpar'

print(f'// {segundo_jogador}, você ficou com {escolha2}.')

numero1 = int(input(f'-> {primeiro_jogador}, escolha um número:'))
numero2 = int(input(f'-> {segundo_jogador}, escolha um número:'))

soma = numero1 = numero2

if soma % 2 == 0:
  vencedor = 'par'
else:
  vencedor = 'ímpar'

if vencedor == escolha:
  print(f'// {primeiro_jogador} venceu!')
else:
  print(f'// {segundo_jogador} venceu!')