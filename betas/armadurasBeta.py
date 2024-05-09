from random import randint
import time

armaduras_raras = ["armadura1", "armadura2", "armadura3", "armadura4", "armadura5"]
armaduras_epicas = ["armadura1", "armadura2", "armadura3", "armadura4", "armadura5"]
armaduras_lendarias = ["armadura1", "armadura2", "armadura3", "armadura4", "armadura5"]
opcoes = [0, 1, 2, 3]
opcoes_venda = [1, 2, 3, 4]
arcanum = None
escolha = 0

arcanum = int(input('\033[1;32mInsira sua quantidade de Arcanums: \033[0m'))
time.sleep(0.5)

print(f'\033[1;31mVocê deseja vender algum item?\033[0m')
time.sleep(0.5)
print('[1] Para Raro | 2 Arcs')
time.sleep(0.5)
print('[2] Para Épico | 3 Arcs')
time.sleep(0.5)
print('[3] Para Lendário | 4 Arcs')
time.sleep(0.5)
print('[4] Não')
time.sleep(1)
escolha_venda = int(input('\033[1;32mEscolha a opção: \033[0m'))
time.sleep(0.5)

while escolha_venda not in opcoes_venda:
    print('opção inválida')
    escolha_venda = int(input('\033[1;32mEscolha a opção: \033[0m'))
    time.sleep(0.5)

while escolha_venda != 4:
    if escolha_venda == 1:
        print(f'\033[1;31mObrigado por vender, você ganhou 2 Arcs\033[0m')
        arcanum +=2
        print(f'Agora você tem {arcanum} Arcs')
    if escolha_venda == 2:
        print(f'\033[1;31mObrigado por vender, você ganhou 3 Arcs\033[0m')
        arcanum +=3
        print(f'Agora você tem {arcanum} Arcs')
    if escolha_venda == 3:
        print(f'\033[1;31mObrigado por vender, você ganhou 4 Arcs\033[0m')
        arcanum +=4
        print(f'Agora você tem {arcanum} Arcs')
    time.sleep(1)
    print(f'\033[1;31mVocê deseja vender mais algum item?\033[0m')
    time.sleep(0.5)
    print('[1] Para Raro | 2 Arcs')
    time.sleep(0.5)
    print('[2] Para Épico | 3 Arcs')
    time.sleep(0.5)
    print('[3] Para Lendário | 4 Arcs')
    time.sleep(0.5)
    print('[4] Não')
    time.sleep(1)
    escolha_venda = int(input('\033[1;32mEscolha a opção: \033[0m'))
    time.sleep(0.5)
    while escolha_venda not in opcoes_venda:
        print('opção inválida')
        escolha_venda = int(input('\033[1;32mEscolha a opção: \033[0m'))
        time.sleep(0.5)

if arcanum >= 4:
    print('\033[1;31mAgora vamos para as armaduras\033[0m')
    print(f'Você tem {arcanum} Arcs')
    time.sleep(0.5)
    print('[1] Para Raro | 4 Arcs')
    time.sleep(0.5)
    print('[2] Para Épico | 6 Arcs')
    time.sleep(0.5)
    print('[3] Para Lendário | 8 Arcs')
    time.sleep(1)
    escolha = int(input('\033[1;32mEscolha a opção: \033[0m'))
    time.sleep(0.5)

while escolha not in opcoes:
    if escolha == 0:
        break
    print('opção inválida')
    escolha = int(input('\033[1;32mEscolha a opção: \033[0m'))
    time.sleep(0.5)
    
if escolha == 1:
    if arcanum >= 4:
        num_aleatorio = randint(0, len(armaduras_raras) - 1)
        armadura = armaduras_raras[num_aleatorio]
        arcanum -= 4
        print(f'Sua armadura é {armadura} e agora você tem {arcanum} arcs')
        time.sleep(0.5)
        compra = 1
    else:
        print('Não tem Arcanums suficiente')
if escolha == 2:
    if arcanum >= 6:
        num_aleatorio = randint(0, len(armaduras_epicas) - 1)
        armadura = armaduras_epicas[num_aleatorio]
        arcanum -= 6
        print(f'Sua armadura é {armadura} e agora você tem {arcanum} arcs')
        time.sleep(0.5)
        compra = 1
    else:
        print('Não tem Arcanums suficiente')
if escolha == 3:
    if arcanum >= 8:
        num_aleatorio = randint(0, len(armaduras_lendarias) - 1)
        armadura = armaduras_lendarias[num_aleatorio]
        arcanum -= 8
        print(f'Sua armadura é {armadura} e agora você tem {arcanum} arcs')
        time.sleep(0.5)
        compra = 1
    else:
        print('Não tem Arcanums suficiente')

if compra == 1:
    print(f'\033[1;31mDesfrute a sua {armadura}, até outro dia\033[0m')
else:
    print(f'\033[1;31mTe faltam {4 - arcanum} arcanums para você realizar uma compra, até um outro dia\033[0m')
        