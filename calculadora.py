
while True:
    num_1 = input('Digite o primeiro numero: ')
    num_2 = input('\nDigite o segundo numero: ')
    operador = input('\nQual a operação deseja realizar? ( + - * / )  ')

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        
        if len(operador) > 1:
            print('Digite apenas um operador!')
        elif operador == '+':
            print (f'\n{num_1_float} + {num_2_float} =',num_1_float + num_2_float)
        elif operador == '-':
            print (f'\n{num_1_float} - {num_2_float} =',num_1_float - num_2_float)
        elif operador == '*':
            print (f'\n{num_1_float} * {num_2_float} =',num_1_float * num_2_float)
        elif operador == '/':
            print (f'\n{num_1_float} / {num_2_float} =',num_1_float / num_2_float)
        else:
            print(f'\nO operador "{operador}" é invalido')

    except Exception as error:
        print(error)
        continue

    
    continuar = input ('\nGostaria de continuar? (s/n)')
    if continuar != 's' and continuar != 'S':
        print('\n')
        break