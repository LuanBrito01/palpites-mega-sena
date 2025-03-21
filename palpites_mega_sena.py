from random import randint
from time import sleep

loteria = []
jogos = []
print('-' * 30)
print(f'{"💰 PALPITES PARA A MEGA SENA 💰":^30}')
print('-' * 30)
qtd= int(input('Quantos serão sorteados? '))
total = 1
while total <= qtd:
    cont = 0
    while True:
        num = randint(1,61)
        if num not in loteria:
            loteria.append(num)
            cont += 1
        if cont >= 6:
            break
    loteria.sort()
    jogos.append(loteria[:])
    loteria.clear()
    total += 1
print()
print(f'-=-' * 3, f' SORTEANDO {qtd} JOGOS ', '-=-' * 3)
print()
for i, j in enumerate(jogos):
    print(f'JOGO {i+1}: {j}')
    sleep(1)
print()
print('-=-' * 3, ' BOA SORTE 🤞🤩 ', '-=-' * 3)



