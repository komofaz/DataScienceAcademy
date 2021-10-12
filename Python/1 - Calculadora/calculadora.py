i = 0
while i == 0 :
    print('1 - Soma')
    print('2 - Divisão')
    print('3 - Multiplicação')
    print('4 - Subtração')
    print('5 - Sair')

    opcao = int(input('Digite uma opção (Ex.: 1) : '))

    if opcao == 5 :
        break

    num1 = float(input('Digite o primeiro número : '))
    num2 = float(input('Digite o segundo número : '))

    if opcao == 1 :
        print('resultado da SOMA é : ' + str(num1 + num2))
    elif opcao == 2 :
        print('resultado da DIVISÃO é : ' + str(num1 / num2))
    elif opcao == 3 :
        print('resultado da MULTIPLICAÇÃO é : ' + str(num1 * num2))
    elif opcao == 4 :
        print('resultado da SUBTRAÇÃO é : ' + str(num1 - num2))
    else:
        print('Opção Inválida')