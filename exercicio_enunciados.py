
# CALCULADORA DE PAR OU IMPAR
#recebe numero
num1 = input('Digite um numero inteiro: ')

try:
#converte para numero inteiro
    num1_int = int(num1)
#verifica se numero é par
    if num1_int%2 == 0:
        print('Seu numero é Par.')
    else:
        print('Seu numero é Impar.')
except:
    print('Seu numero não é um numero inteiro.')

# SAUDAÇÃO CONFORME HORARIO
#recebe hora no formato 24H
hora = input('Qual hora é agora? (24H) ')


try:
#converte para numero inteiro
    hora_int = int(hora)
    if hora_int >= 0 and hora_int < 24:
#verifica se é manhã
        if hora_int < 12 and hora_int > 7:
            print('Então, Bom dia')
    #verifica se é de tarde
        elif hora_int < 19 and hora_int < 24:
            print('Então, Boa tarde')
    #se não for nenhuma anterior, é noite
        else:
            print('Então, Boa noite')
    else:
        print('Favor digite apenas a hora do dia no formato 24H')

    #caso informe mais de um numero
except:    
    print('Favor digite apenas a hora do dia no formato 24H')



nome = input('Digite seu primeiro nome: ')
#verifica se foi digitado apenas um nome

if ' ' not in nome:

#baseado na quantidade de letras, passa a mensagem correta
    if len(nome) < 5:
        print('Seu nome é curto')

    elif len(nome) < 7:
        print('Seu nome é normal')

    else:
        print('Que nomezão!!!')

#caso não seja informado apenas um nome
else:
    print('Digite apenas o primeiro nome!')