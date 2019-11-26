import time


def main():
    print('Bienvenido/a a Convertor de Unidades de Longitud\n')
    print('Convertir desde: ')

    opcion = ''
    while opcion not in ('mm', 'cm', 'm', 'km', 'ml', 'yar'):
        opcion = input('Elige opcion < mm, cm, m, km, ml, yar >: ')
        if opcion not in ('mm', 'cm', 'm', 'km', 'ml', 'yar'):
            print("Por favor, ingrese una opcion valida")

    if opcion == 'mm':
        print('\nConvertir a: ')

        conv = ''
        while conv not in ('cm', 'm', 'km', 'ml', 'yar'):
            conv = input('Elige opcion < cm, m, km, ml, yar >:  ')
            if conv not in ('cm', 'm', 'km', 'ml', 'yar'):
                print("Por favor, ingrese una opcion valida")

        if conv == 'cm':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 10, 'centimetros')
        elif conv == 'm':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 1000, 'metros')
        elif conv == 'km':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 1000000, 'kilometros')
        elif conv == 'ml':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 1609000, 'millas')
        elif conv == 'yar':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 914.4, 'yardas')


    if opcion == 'cm':
        print('\nConvertir a: ')

        conv = ''
        while conv not in ('mm', 'm', 'km', 'ml', 'yar'):
            conv = input('Elige opcion < mm, m, km, ml, yar >:  ')
            if conv not in ('mm', 'm', 'km', 'ml', 'yar'):
                print("Por favor, ingrese una opcion valida")

        if conv == 'mm':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad * 10, 'milimetros')
        elif conv == 'm':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 100, 'metros')
        elif conv == 'km':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 1000, 'kilometros')
        elif conv == 'ml':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 160934.4, 'millas')
        elif conv == 'yar':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 91.44, 'yardas')


    elif opcion == 'm':
        print('\nConvertir a: ')
        
        conv = ''
        while conv not in ('cm', 'km'):
            conv = input('Elige opcion < cm, km >:  ')
            if conv not in ('cm', 'km'):
                print("Por favor, ingrese una opcion valida")

        if conv == 'cm':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad * 100, 'centimetros')
        elif conv == 'km':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 1000, 'kilometros')

    elif opcion == 'km':
        print('\nConvertir a: ')

        conv = ''
        while conv not in ('cm', 'm'):
            conv = input('Elige opcion < cm, m >:  ')
            if conv not in ('cm', 'm'):
                print("Por favor, ingrese una opcion valida")

        if conv == 'cm':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad * 100000, 'centimetros')
        elif conv == 'm':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad * 1000, 'metros')

main()
