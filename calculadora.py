# Calculadora simples com repetição e tratamento de erros

# O programa roda indefinidamente até o usuário escolher sair
while True:
    # Entrada dos números e do operador
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('\nDigite o segundo número: ')
    operador = input('\nQual operação deseja realizar? ( +  -  *  / )  ')

    try:
        # Conversão das entradas para número decimal (float)
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        
        # Verifica se o operador tem mais de um caractere (inválido)
        if len(operador) > 1:
            print('Digite apenas um operador!')
        
        # Realiza a operação conforme o operador escolhido
        elif operador == '+':
            print(f'\n{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
        
        elif operador == '-':
            print(f'\n{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
        
        elif operador == '*':
            print(f'\n{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
        
        elif operador == '/':
            # Evita erro de divisão por zero
            if num_2_float == 0:
                print('\nErro: divisão por zero não é permitida!')
            else:
                print(f'\n{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
        
        else:
            # Caso o operador não seja reconhecido
            print(f'\nO operador "{operador}" é inválido.')

    except:
        # Tratamento de erro para entradas que não podem ser convertidas para float
        print('\nErro: Por favor, digite números válidos!') 

    # Pergunta se o usuário deseja continuar
    continuar = input('\nGostaria de continuar? (s/n): ')
    if continuar.lower() != 's':  # Se não digitar 's' ou 'S', encerra
        print('\nEncerrando o programa...\n')
        break
# Fim do loop, o programa encerra