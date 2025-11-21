import random
import sys

nove_digito = ''
ver1=0
ver2=0

for i in range(9):
    nove_digito += str(random.randint(0,9))

print(f' Os priemiros 9 digitos são: {nove_digito}')
entrada_sequencial = nove_digito == nove_digito[0] * len(nove_digito)
    
if entrada_sequencial:
    print("CPF inválido. Todos os dígitos não podem ser iguais.")
    sys.exit()

contador_regressivo = 10
for digito in nove_digito:
    ver1 += int(digito) * contador_regressivo
    contador_regressivo -= 1

ver1 = ver1 * 10 % 11
ver1 = 0 if ver1 > 9 else ver1
dez_digito = nove_digito + str(ver1)

print(f' O primeiro dígito verificador é: {ver1}')

contador_regressivo = 11
for digito in dez_digito:
    ver2 += int(digito) * contador_regressivo
    contador_regressivo -= 1

ver2 = ver2 * 10 % 11
ver2 = 0 if ver2 > 9 else ver2 
cpf_gerado = dez_digito + str(ver2)

print(f' O segundo dígito verificador é: {ver2}')

print(f'O CPF gerado foi: {cpf_gerado}')