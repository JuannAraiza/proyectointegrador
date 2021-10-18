import math 
def main():
    #escribe tu código abajo de esta línea
    print('Este es un programa acerca del Coronavirus')
    print('------------------------------------------')
    nombre= input('Hola, ¿Cual es tu nombre?: ')
    print(f'Bienvenido {nombre} esperamos que te encuentres de lo mejor!')

    input('Presiona <enter> para continuar')

    print('¿Qué es lo que deseas investigar el día de hoy?')
    print('1. Información del Coronavirus     2. Test rápido      3. Casos en México        4. Recomendaciones      5. Salir del programa')
    a = int(input('Porfavor dinos tu elección(introduce solamente el número): '))
    while a < 1 or a > 5:
        print('Porfavor introduce un número válido')
        a = int(input(''))
    if a == 1:
            print('')
    elif a == 2:
        print('A continuación se presentará un test rápido de COVID-19!(contesta con si o no) ')
        s = 0
        b = input('Tienes temperatura de > 37.5º?: ')
        c = input('Sientes tos?: ')
        d = input('Sientes dificultad para respirar?: ')
        e = input('Eres capaz de percibir sabores?: ')
        f = input('Sientes dolor muscular?: ')
        if b == ('si'):
            s =+ 1
        elif c == ('si'):
            s =+1
        elif d == ('si'):
            s =+ 1
        elif e == ('no'):
            s =+ 1
        elif f == ('si'):
            s =+ 1
        if s > 0:
            print('CUIDADO!, es probable que seas positivo al COVID-19')
            print('¡De todas maneras visita a un médico profesional para que se te haga la prueba necesaria')
            print('y no tomes como única evidencia o prueba este test rápido!')
        else:
            print('¡Enhorabuena! no sientes ningún sintoma común del COVID-19')   
    elif a == 4:


        





        




if __name__=='__main__':
    main()
