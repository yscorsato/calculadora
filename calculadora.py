while True:
    print('1 para soma')
    print('2 para subtraçao')
    print('3 para divisão')
    print('4 para murltiplicao')
    print('5 para Sair do sitema')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    n = int(input('Escolha a operção: '))

    if n == 1:
        print('Vamos somar')
        print('')
        n1 = int(input('Numero1: '))
        n2 = int(input('Numero2: '))
        r = n1 + n2
        print(f'Resultado: {r}')


    if n == 2:
        print('Vamos subtração')
        print('')
        n1 = int(input('Numero1: '))
        n2 = int(input('Numero2: '))
        r = n1 - n2
        print(f'Resultado: {r}')

    if n == 3:
        print('Vamos divisao')
        print('')

        n1 = int(input('Numero1: '))
        apoio = 1
        while apoio >= 1: # laço de repetição so repete se for verdade
            n2 = int(input('Numero2: '))
            if n2 >=1:
                apoio = 0

            r = n1 / n2

        print(f'Resultado: {n1} / {n2} = {r}')
        print('')

    if n == 4:
        print('Vamos mutiplicao')
        print('')
        n1 = int(input('Numero1: '))
        n2 = int(input('Numero2: '))
        r = n1 * n2
        print(f'Resultado: {r}')

    if n >=5:
        print('Fim')
        break





