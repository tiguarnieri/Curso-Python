nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:

    print(f'\nSeu nome é "{nome}"')
    print(f'Seu nome invertido é "{nome[::-1]}"')
    if ' ' in nome:
        print(f'Seu nome contem espaços')
    else:
        print(f'Seu nome não contem espaços')
    print(f'Seu nome tem "{len(nome)}" letras')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A ultima letra do seu nome é "{nome[-1]}"\n')

else:
    print('Desculpe, você deixou algum campo vazio!')