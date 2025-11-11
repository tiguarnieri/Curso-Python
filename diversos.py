lista = []

while True:
    print(f'Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar\n').lower

    if opcao == 'i':
        valor = input(f'Valor: ').lower
        lista = lista.append(valor)
