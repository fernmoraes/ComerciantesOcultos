#Bibliotecas
import random
import time

#Variaveis
armas_raras = ["Terremoto", "Agulha Escarlate", "Silver Dragon", "Ruina dos dragões",]
armas_epicas = ["Chama da Fênix", "Tsunami", "A primeira Arma",]
armas_lendarias = ["Rios de Sangue", "Nevermiss", "Ethernal Echoes",]
opcoes = [0, 1, 2, 3]
opcoes_venda = [1, 2, 3, 4]
arcanum = None
escolha = 0
compra = None
raridade = 1

arcanum = int(input('\033[1;32mInsira sua quantidade de Arcanums: \033[0m'))#Pedido dos Arcanums
time.sleep(0.5)

print(f'\033[1;31mVocê deseja vender algum item?\033[0m')#Venda de itens
time.sleep(0.3)
print('[1] Para Raro | 2 Arcs')
time.sleep(0.3)
print('[2] Para Épico | 3 Arcs')
time.sleep(0.3)
print('[3] Para Lendário | 4 Arcs')
time.sleep(0.3)
print('[4] Não')
time.sleep(0.5)
escolha_venda = int(input('\033[1;32mEscolha a opção: \033[0m'))
time.sleep(0.3)
while escolha_venda not in opcoes_venda:
    print('opção inválida')
    escolha_venda = int(input('\033[1;32mEscolha a opção: \033[0m'))
    time.sleep(0.3)

while escolha_venda != 4:#Função Venda
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
    time.sleep(0.5)
    print(f'\033[1;31mVocê deseja vender mais algum item?\033[0m')#Vender mais
    time.sleep(0.3)
    print('[1] Para Raro | 2 Arcs')
    time.sleep(0.3)
    print('[2] Para Épico | 3 Arcs')
    time.sleep(0.3)
    print('[3] Para Lendário | 4 Arcs')
    time.sleep(0.3)
    print('[4] Não')
    time.sleep(0.5)
    escolha_venda = int(input('\033[1;32mEscolha a opção: \033[0m'))
    time.sleep(0.3)
    while escolha_venda not in opcoes_venda:
        print('opção inválida')
        escolha_venda = int(input('\033[1;32mEscolha a opção: \033[0m'))
        time.sleep(0.3)

print('\033[1;31mAgora vamos para os pacotes de armas\033[0m')#Compra dos pacotes
print(f'Você tem {arcanum} Arcs')
time.sleep(0.3)
print('[1] Pacote dos Tesouros Raros | 4 Arcs')
time.sleep(0.3)
print('[2] Pacote dos Artefatos Épicos | 6 Arcs')
time.sleep(0.3)
print('[3] Pacote das Relíquias Lendárias | 8 Arcs')
time.sleep(0.5)
escolha = int(input('\033[1;32mEscolha a opção: \033[0m'))
time.sleep(0.3)

while escolha not in opcoes:
    if escolha == 0:
        break
    print('opção inválida')
    escolha = int(input('\033[1;32mEscolha a opção: \033[0m'))
    time.sleep(0.3)

# Definindo as probabilidades de cada tipo de arma para cada pacote
pacote1 = {"rara": 0.6, "epica": 0.3, "lendaria": 0.1}
pacote2 = {"rara": 0.3, "epica": 0.4, "lendaria": 0.2}
pacote3 = {"rara": 0.1, "epica": 0.4, "lendaria": 0.5}

# Dicionário com o custo de cada pacote
custo_pacotes = {1: 4, 2: 6, 3: 8}
    
def abrir_pacote(pacote, custo, arcanum):
    if arcanum < custo:
        print(f'\033[1;31mTe faltam {custo - arcanum} arcanums para você realizar uma compra, até um outro dia\033[0m')
        return None

    probabilidade = random.random()
    if probabilidade < pacote["rara"]:
        return random.choice(armas_raras)  # Escolhe uma arma rara aleatoriamente
    elif probabilidade < pacote["rara"] + pacote["epica"]:
        return random.choice(armas_epicas)  # Escolhe uma arma épica aleatoriamente
    else:
        return random.choice(armas_lendarias)  # Escolhe uma arma lendária aleatoriamente

# Verificando se a entrada do usuário é válida
if escolha not in custo_pacotes:
    print("Escolha de pacote inválida!")
else:
    moedas = arcanum  # Definindo o número de moedas disponíveis
    resultado = abrir_pacote(eval(f"pacote{escolha}"), custo_pacotes[escolha], arcanum)
    if resultado in armas_raras:
        print(f'\033[1;31mDesfrute a sua arma rara: \033[1;34m{resultado}\033[1;31m, até outro dia!\033[0m')
        arcanum -= custo_pacotes[escolha]
        print("Moedas restantes:", arcanum)   
    elif resultado in armas_epicas:
        print(f'\033[1;31mDesfrute a sua arma épica: \033[1;35m{resultado}\033[1;31m, até outro dia!\033[0m')
        arcanum -= custo_pacotes[escolha]
        print("Moedas restantes:", arcanum)    
    elif resultado in armas_lendarias:
        print(f'\033[1;31mDesfrute a sua arma lendária: \033[1;33m{resultado}\033[1;31m, até outro dia!\033[0m')
        arcanum -= custo_pacotes[escolha]
        print("Moedas restantes:", arcanum)  