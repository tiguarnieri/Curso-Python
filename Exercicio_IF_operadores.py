# Programa que compara dois números informados pelo usuário

# Solicita os dois números (entradas são sempre strings)
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

# Exibe os números escolhidos
print(f'\nOs números escolhidos foram: {num1} e {num2}\n')

# Estrutura condicional para verificar qual é maior
# ou se são iguais
# Utiliza operadores de comparação para determinar o maior número

if num1 > num2:
    print(f'O número {num1} é maior.\n')
elif num2 > num1:
    print(f'O número {num2} é maior.\n')
else:
    print('Os números são iguais.\n')
# Exibe uma mensagem final
print('Fim do programa.')