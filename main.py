tableroPrueba = [[0,1,0],[0,0,1],[5,5,0]]

'''
Esta función inicializa un tablero
'''
def inicializarTablero():
    return [[0,0,0],[0,0,0],[0,0,0]]
'''
Esta función nos pinta un tablero dado un tablero
'''
def pintarTablero(tablero):
    print("Tablero: ")
    for i in range(0, len(tablero)):
        salida = ""
        for j in range(0, len(tablero[i])):
            valor = tablero[i][j]
            salida += "|"
            if(valor == 1):
                salida +=('X')
            elif(valor ==5):
                salida +=('O')
            else:
                salida +=(' ')
        salida += "|"
        print(salida)


'''
Función que devuelve el jugador ganador si lo hay
         1: Si gana el jugador 1
         5: Si gana el jugador 5
         0: Si es empate
        -1: Si todavía se esta jugando
'''
def esGanador(tablero):
    
    pass
     
pintarTablero(tableroPrueba)
