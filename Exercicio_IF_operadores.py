num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

print(f'\nOs numeros escolhidos foram: {num1} e {num2}\n')

if num1 > num2:
    print(f'O numero {num1} é maior.\n')
elif num2 > num1:
    print(f'O numero {num2} é maior.\n')
else:
    print(f'Os numeros são iguais.\n')
