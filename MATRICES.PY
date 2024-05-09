juego = [['☂','☂','☂','☂','☂'],['☂','☂','☂','☂','☂'],['☂','☂','☂','☂','☂'],['☂','☂','☂','☂','☂'],['☂','☂','☂','☂','☂']]

import os
contador = -1

def fnt_limpiar ():
    os.system('cls')
    print('AUTOR: JUAN JOSE HERNANDEZ ')
    print('\n')
    fnt_impresion()
  

def fnt_impresion():
    global contador
    for i in range(len(juego)):
        for j in range(len(juego[i])):
            print(juego[i][j], end = '  ')
        
        print()
    contador +=1
    print(f'intentos {contador } ')
    
        
        
def fnt_agregar(x,y,):
    if x == 0 and y == 0:
        juego[x][y]= '✔'
    elif x == 0 and y == 1:
        juego[x][y] = '✔'
    elif x== 0 and y== 2:
        juego[x][y]= '✔'
    elif x == 0 and y == 3:
        juego[x][y] = '✔'
    elif x== 0 and y== 4:
        juego[x][y]= '✔'
    elif x == 1 and y == 0:
        juego[x][y] = '✔'
    elif x== 1 and y== 1:
        juego[x][y]= '✘'
    elif x== 1 and y == 2:
        juego[x][y] = '✘'
    elif x== 1 and y == 3:
        juego[x][y] = '✘'
    elif x== 1 and y == 4:
        juego[x][y]= '✔'
    elif x == 2 and y == 0:
        juego[x][y]= '✔'
    elif x == 2 and y == 1:
        juego[x][y] = '✔'
    elif x== 2 and y== 2:
        juego[x][y]= '✔'
    elif x == 2 and y == 3:
        juego[x][y] = '✔'
    elif x== 2 and y== 4:
        juego[x][y]= '✔'
    elif x == 3 and y == 0:
        juego[x][y] = '✔'
    elif x== 3 and y== 1:
        juego[x][y]= '✘'
    elif x== 3 and y == 2:
        juego[x][y] = '✘'
    elif x== 3 and y == 3:
        juego[x][y] = '✘'
    elif x== 3 and y == 4:
        juego[x][y]= '✔'
    elif x == 4 and y == 0:
        juego[x][y] = '✔'
    elif x== 4 and y== 1:
        juego[x][y]= '✘'
    elif x== 4 and y == 2:
        juego[x][y] = '✘'
    elif x== 4 and y == 3:
        juego[x][y] = '✘'
    elif x== 4 and y == 4:
        juego[x][y]= '✔'

sw = True
while sw == True:
    fnt_limpiar()
    fnt_agregar(int(input('fila: ')), int(input('columna: ')))
    
        