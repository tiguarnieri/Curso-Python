cpf = input("Digite o CPF (apenas números): ").replace('.','').replace('-','')  # Pede que o usuário digite o CPF

if not cpf.isdigit():  # Verifica se todos os caracteres digitados são números

    print("CPF inválido. Por favor, insira apenas números.")  
    
else:
    # Converte cada posição do CPF em um número inteiro separado
    num1 = int(cpf[0])
    num2 = int(cpf[1]) 
    num3 = int(cpf[2])
    num4 = int(cpf[3])
    num5 = int(cpf[4])
    num6 = int(cpf[5])
    num7 = int(cpf[6])
    num8 = int(cpf[7])
    num9 = int(cpf[8])
    num10 = int(cpf[9])   # Primeiro dígito verificador do CPF informado
    num11 = int(cpf[10])  # Segundo dígito verificador do CPF informado

    # Verifica se todos os números do CPF são iguais (ex: 111.111.111-11)
    if (num1 == num2 == num3 == num4 == num5 == num6 == num7 == num8 == num9 == num10 == num11):
        print("CPF inválido. Todos os dígitos não podem ser iguais.")

    else:
        # Cálculo do primeiro dígito verificador usando a fórmula oficial
        ver1 = ((num1 * 10 + num2 * 9 + num3 * 8 + num4 * 7 + num5 * 6 +
                 num6 * 5 + num7 * 4 + num8 * 3 + num9 * 2) * 10) % 11

        ver1 = 0 if ver1 > 9 else ver1  # Se der 10 ou 11, o dígito vira 0

    # Cálculo do segundo dígito verificador usando o primeiro como parte da conta
    ver2 = ((num1 * 11 + num2 * 10 + num3 * 9 + num4 * 8 + num5 * 7 +
             num6 * 6 + num7 * 5 + num8 * 4 + num9 * 3 + ver1 * 2) * 10) % 11

    ver2 = 0 if ver2 > 9 else ver2  # Ajuste do segundo dígito se o resultado for maior que 9

    # Verificação se os dígitos calculados batem com os dígitos do CPF digitado
    if ver1 == num10 and ver2 == num11:
        print("O primeiro dígito verificador é:", ver1)  
        print("O segundo dígito verificador é:", ver2)
        print("CPF válido.")  # CPF está correto
    else:
        print("CPF inválido. Os dígitos verificadores não correspondem.")  # CPF errado
        print("O primeiro dígito verificador deveria ser:", ver1)
        print("O segundo dígito verificador deveria ser:", ver2)    