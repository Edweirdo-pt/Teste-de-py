"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
nome_invert = f'{nome[::-1]}'

if nome == '' or idade == '':
    print('Desculpe, vocês deixou campos em branco')

if nome  and idade:
    print(f'O seu nome é {nome}')
    print(f'O seu nome invertido é {nome[::-1]}')

if ' ' in nome:
    print('Seu nome contem espaços')
else:
    print(f'{nome} não contem espaços!')

if nome and idade:
    print(f'A primeira letra do seu nome é: {nome[0:1:]}')
    print(f'A ultima letra do seu nome é: {nome_invert[0:1:]}')
    
