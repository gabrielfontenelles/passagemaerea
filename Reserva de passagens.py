import os
import random
import time

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu(*opcoes):
    op_disp = []
    for x in range(len(opcoes)):
        print(f'{x + 1} - {opcoes[x]}')
        op_disp.append(str(x + 1))
    opcao = ''
    while opcao not in op_disp:
        opcao = input('Escolha uma opção: ')
        if(opcao not in op_disp):
            print('Opção inválida!\n')
    return opcao

def titulo(texto):
    print(f'{50 * "-"}')
    print('{:^50}'.format(texto))
    print(f'{50 * "-"}')

voos = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012']
origens = ['Goiânia', 'Campo Grande', 'Goiânia', 'Goiânia', 'Brasília', 'Cuiabá', 'Salvador', 'Porto Seguro', 'Aracaju', 'Vitória', 'Campinas - SP', 'Florianópolis']
destinos = ['Campo Grande', 'Corumbá - MS', 'Ponta Porã', 'Cuiabá', 'Aracajú', 'Goiânia', 'Goiânia', 'Goiânia', 'Brasília', 'Campinas - SP', 'Vitória', 'Goiânia']
lugares = random.sample(range(0, 15), 12) #[1,0,0,0,0,0,0,0,0,0,0,0]

'''for x in range(12):
    titulo('Armazenando as Informações Sobre os Voos')
    num = input(f'Digite o número do voo para o {x + 1}º avião: ')
    while num in voos:
        num = input(f'Número do Vôo já existe!\nDigite o número do voo para o {x + 1}º avião: ')
    voos.append(num)
    origens.append(input('Digite a origem do voo: ').capitalize())
    destinos.append(input('Digite o destino do voo: ').capitalize())
    qtd_disp = -1
    while qtd_disp < 0:
        try:
            qtd_disp = int(input('Digite a quantidade de lugares disponível para esse voo: '))
        except:
            print('O valor digitado é inválido!')
    limparTela()'''

opcao = ''
while opcao != '3':
    limparTela()
    titulo('Agência de Viagens')
    opcao = menu('Consultar', 'Efetuar Reserva', 'Sair')

    limparTela()
    match opcao:
        case '1':
            titulo('Consultar Vôo')
            opcao = menu('Por número de voo', 'Por origem', 'Por destino')
            limparTela()
            match opcao:
                case '1':
                    titulo('Consulta por número do voo')
                    num = input('\nInforme o número do voo: ')
                    if(num in voos):
                        limparTela()
                        titulo('Detalhes do Voo')
                        indice = voos.index(num)
                        print(f'Número do voo: {num}\nOrigem: {origens[indice]}\nDestino: {destinos[indice]}\nLugares Disponíveis: {lugares[indice]}')
                        input('\nPressione qualquer tecla para continuar...')
                    else:
                        input('\nVoo não encontrado!\n\nPressione qualquer tecla para continuar...')
                case '2':
                    titulo('Consulta por origem')
                    origem = input('Digite a origem do voo: ').capitalize()
                    if(origem in origens):
                        limparTela()
                        titulo('Voos Encontrados')
                        for x in range(len(origens)):
                            if(origens[x] == origem):
                                print(f'Número do voo: {voos[x]}, Origem: {origem}, Destino: {destinos[x]}, Lugares Disponíveis: {lugares[x]}')
                        input('\nPressione qualquer tecla para continuar...')
                    else:
                        input('\nOrigem não encontrada!\n\nPressione qualquer tecla para continuar...')
                case '3':
                    opcao = ''
                    titulo('Consulta por destino')
                    destino = input('Digite o destino do voo: ').capitalize()
                    if (destino in destinos):
                        limparTela()
                        titulo('Voos Encontrados')
                        for x in range(len(destinos)):
                            if (destinos[x] == destino):
                                print(
                                    f'Número do voo: {voos[x]}, Origem: {origens[x]}, Destino: {destino}, Lugares Disponíveis: {lugares[x]}')
                        input('\nPressione qualquer tecla para continuar...')
                    else:
                        input('\nDestino não encontrado!\n\nPressione qualquer tecla para continuar...')
        case '2':
            titulo('Efetuar Reserva')
            num = input('Informe o número do voo: ')
            if (num in voos):
                indice = voos.index(num)
                if(lugares[indice] > 0):
                    limparTela()
                    titulo('Confirmação de Reserva')
                    lugares[indice] -= 1
                    input('\nReserva confirmada!\n\nPressione qualquer tecla para continuar...')
                else:
                    input('\nVoo lotado!\n\nPressione qualquer tecla para continuar...')
            else:
                input('\nVoo inexistente!\n\nPressione qualquer tecla para continuar...')
        case '3':
            titulo('Encerrando a aplicação...')
            time.sleep(3)

