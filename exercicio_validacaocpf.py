cpf = input("Digite o CPF (apenas números): ")

for digito in cpf:
    if not digito.isdigit():
        print("CPF inválido. Por favor, insira apenas números.")
        break
    if len(cpf) != 11:   
        print("CPF inválido. O CPF deve ter 11 dígitos.")
        break
    else:

        num1 = int(cpf[0])
        num2 = int(cpf[1]) 
        num3 = int(cpf[2])
        num4 = int(cpf[3])
        num5 = int(cpf[4])
        num6 = int(cpf[5])
        num7 = int(cpf[6])
        num8 = int(cpf[7])
        num9 = int(cpf[8])
        num10 = int(cpf[9])
        num11 = int(cpf[10])

        if (num1 == num2 == num3 == num4 == num5 == num6 == num7 == num8 == num9 == num10 == num11):
            print("CPF inválido. Todos os dígitos não podem ser iguais.")

        else:
            validacao = ((num1 * 10 + num2 * 9 + num3 * 8 + num4 * 7 + num5 * 6 + num6 * 5 + num7 * 4 + num8 * 3 + num9 * 2) *10)% 11
            0 if validacao > 9 else validacao
        if validacao == num10:
                print("CPF válido.")
        else:
                print("CPF inválido. O primeiro dígito verificador não confere.")