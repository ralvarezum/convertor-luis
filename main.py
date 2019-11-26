import time


def main():
    print('Bienvenido/a a Convertor de Unidades de Longitud\n')
    print('Convertir desde: ')

    opcion = ''
    while opcion not in ('cm', 'm', 'km'):
        opcion = input('Elige opcion < cm, m, km >: ')
        if opcion not in ('cm', 'm', 'km'):
            print("Por favor, ingrese una opcion valida")



    if opcion == 'cm':
        print('\nConvertir a: ')
        conv = input('Elige opcion < m, km >:  ')
        if conv == 'm':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 100, 'metros')
        elif conv == 'km':
            cantidad = float(input('\nIndica la cantidad a convertir: '))
            print('Calculando..............')
            time.sleep(5)
            print(cantidad / 1000, 'kilometros')

    elif opcion == 'm':
        print('\nConvertir a: ')
        conv = input('Elige opcion < cm, km >:  ')
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
        conv = input('Elige opcion < cm, m >:  ')
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
