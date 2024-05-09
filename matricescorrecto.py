juego = [['☢','☢','☢','☢','☢'],
         ['☢','☢','☢','☢','☢'],
         ['☢','☢','☢','☢','☢'],
         ['☢','☢','☢','☢','☢'],
         ['☢','☢','☢','☢','☢']]

correcto = '⚑'
incorrecto = '⚐'
list_pregunta = ['¿Que es python ?\n\n1. juego \n2. lenguaje de programacion  \n3. marca de agua \n4. ninguna de las    anteriores ',
'¿Que es HTML? \n1. lenguaje de maquetacion \n2. marca de gaseosa \n3. navegador \n4. perro caliente ',
'¿Que es el agua? \n1. ']
list_respuesta = ['2','1']

import os
    
    
    
    
def fnt_impresion():
    global contador
    for i in range(len(juego)):
        for j in range(len(juego[i])):
            print(juego[i][j], end = '   ')
        
        print('\n')

sw = True
contador= 0

    
for i in range(len(juego)):
    for j in range(len(juego[i])):
        import os
        os.system('cls')
        fnt_impresion()
        print()
        print(list_pregunta[contador])
        print()
        r = input('-> ')
        if r == list_respuesta[contador]:
            juego[i][j] = correcto
        else:
            juego[i][j] = incorrecto
        contador += 1