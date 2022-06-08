'''
Faça um programa de numeros premiados em que o usuário deve acertar todos os 4 números para ganhar o prêmio,
o programa deve escrever na tela se o usuário venceu ou perdeu
'''
from random import choice
print('-=-'* 26)
print('Acerte os quatro numeros premiados entre 1 e 20 para ganhar seu prêmio em dinheiro')
print('-=-'* 26)
#Define os numeros na lista
lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8, 10]
lista3 = [11, 13, 15, 17, 19]
lista4 = [12, 14, 16, 18, 20]
#O programa escolhe os numeros dentro da lista
numero1 = choice(lista1)
numero2 = choice(lista2)
numero3 = choice(lista3)
numero4 = choice(lista4)
#O usuário escolhe os numeros
escolha1 = int(input(f'Digite o primeiro numero: '))
escolha2 = int(input(f'Digite o segundo numero: '))
escolha3 = int(input(f'Digite o terceiro numero: '))
escolha4 = int(input(f'Digite o quarto numero: '))
#O programa define  se ele acertou todos os numeros ou não
if escolha1 == numero1 and escolha2 == numero2 and escolha3 == numero3 and escolha4 == numero4:
   print(f'Parabéns! Você acertou todos os numeros e ganhou R$1000, os números eram {numero1}, {numero2}, {numero3}, {numero4}.')
else:
    print(f'Você não acertou todos os numeros, eles eram {numero1}, {numero2}, {numero3}, {numero4}.')
