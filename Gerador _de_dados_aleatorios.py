import random
import Gerador_de_dados_aleatorios.lista as lista
import os
print('-='*20)
print('BEM VINDO AO GERADOR DE DADOS')
print('-='*20)

while True:
    menu = input('''Escolha as opções abaixo
    [1] - NOME
    [2] - CIDADE
    [3] - EMAIL
    [4] - ESTADO
    [5] - TELEFONE   
    [6] - PARAR
    Suas opçãos:  ''')

    print('-='*20)

    menu2 = str(input('Deseja salvar os arquivos em um TXT?[S/N]')).upper().strip()

    opcao_menu = menu.replace(',',' ') 
    

    def processamento_de_dados(dados):
        output =''

        if '1' in dados:
            nomes = random.choice(lista.nomes)
            output = output + nomes + '\n'
        if '2' in dados:
            cidade = random.choice(lista.cidade)  
            output = output + cidade + '\n'
        if '3' in dados:
            email = random.choice(lista.email)
            output = output + email + '\n'
        if '4' in dados:
            estado = random.choice(lista.estado)
            output = output + estado + '\n'
        if '5' in dados:
            telefone = random.choice(lista.telefone)
            output = output + telefone + '\n'

        return output 
    
    arquivos = processamento_de_dados(menu)
    print(arquivos)

    if menu2 == 'S':
        with open('selecionados.txt','w', encoding='utf-8') as arquivo:
            arquivo.write(arquivos)
            