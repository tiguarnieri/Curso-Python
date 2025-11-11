# Programa que analisa o nome e a idade informados pelo usuário

# Solicita o nome e a idade
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

# Verifica se o usuário digitou algo em ambos os campos
if nome and idade:

    # Exibe o nome
    print(f'\nSeu nome é "{nome}"')

    # Mostra o nome invertido (usando fatiamento de string)
    print(f'Seu nome invertido é "{nome[::-1]}"')

    # Verifica se o nome contém espaços
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    # Mostra o total de caracteres do nome (contando espaços)
    print(f'Seu nome tem "{len(nome)}" letras')

    # Mostra a primeira e a última letra do nome
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A última letra do seu nome é "{nome[-1]}"\n')

# Caso o usuário não preencha algum campo
else:
    print('Desculpe, você deixou algum campo vazio!')
