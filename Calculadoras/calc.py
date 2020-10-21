x = y = z = res = 0
cont = 's'

while cont == 's':
    while True:
        try:
            x = float(input('Digite o primeiro numero '))
            y = float(input('Digite o segundo numero '))
            z = int(input('''   Escolha uma operação matematica:
                1 - Soma
                2 - Subtração
                3 - Multiplicação
                4 - Divisão
                ... '''))
        except ValueError as e:
            print('Isso não me parece um número! ;-;')
        else:
            break

    while z == 4 and y == 0:
        print('[ERRO]: Não é possivel dividir por 0!')
        y = float(input('Digite o segundo numero '))
        z = int(input('''   Escolha uma operação matematica:
        1 - Soma
        2- Subtração
        3 - Multiplicação
        4 - Divisão
        ... '''))

    while z > 4 or z < 1:
        print('Operação invalida!')
        z = int(input('''   Escolha uma operação matematica:
        1 - Soma
        2- Subtração
        3 - Multiplicação
        4 - Divisão
        ... '''))

    if z == 1:
        res = x + y
        print(f'A soma de de {x} + {y} é {res}')
    elif z == 2:
        res = x - y
        print(f'A subtração de de {x} - {y} é {res}')
    elif z == 3:
        res = x * y
        print(f'A multiplicação de de {x} x {y} é {res}')
    else:
        res = x / y
        print(f'A divição de de {x} / {y} é {res}')

    cont = input('''  Deseja continuar (s ou n):
    OBS: Qualquer outro caractere será considerado como "n"
    ... ''')

