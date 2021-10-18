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
    a = 0
    while a == 0:
        x = int(input('Porfavor dinos el númerode tu elección(introduce solamente el número): '))
        while x < 1 or x > 5:
            print('Porfavor introduce un número válido')
            x = int(input(''))
        if x == 1:
            print('Información escencial acerca del Coronavirus SARS-Cov-2')
            input('Presiona <ENTER> para continuar')
            print('Toda la información es brindada por el gobierno de México')
            input('Presiona <ENTER> para continuar')
            print('¿Qué es lo que deseas saber acerca del coronavirus?')
            print('(1)¿Qué es? (2)¿Cuáles son los sintomas? (3)¿Cuáles son las personas más vulnerables? (4)¿Qué hacer si tengo sintomas?')
            l = 0
            while l == 0:
                n = int(input('Elige una de las opciones (coloca solamente el número): '))
                while n < 1 or n > 4:
                    print('Porfavor introduce un número válido')
                    n = int(input(''))
                if n == 1:
                    print('¿Qué es el COVID-19?')
                    input('')
                    print('El coronavirus o también llamado COVID-19 es un virus proveniente de China de un origen desconocido,')
                    print('que aunque se tiene sospechas o ideas de donde surgió, todavía no se tiene el dato comprobado o ')    
                    print('confirmado por alguna institución, se dice que es un virus que surgió a partir del murcielago, ya que')
                    print('allá en Wuhan, que es de la ciudad donde surgió el virus, es muy común comer este tipo de alimento,')
                    print('a partir de ahi el virus a ser altamente contagioso se fue expandiendo por todo el mundo, provocando asi')
                    print('una pandemia a nivel mundial la cual, desafortunadamente a acabado con la vida de millones de personas, y')
                    print('que todavía en la actualidad sigue con un auge muy grande.') 
                    
                elif n == 4:
                    l =+1
        elif x == 2:
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
        elif x == 5:
            a =+1
    print('Adiós! Nos vemos pronto!') 
         

if __name__=='__main__':
    main()
