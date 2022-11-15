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
    Devolverá
       1: Si gana el jugador 1
       5: Si gana el jugador 2
       0: Si es empate
      -1: Si se esta jugando
'''
def esGanador(tablero):
    if(ganadorJug1(tablero)):
        return 1
    elif(ganadorJug2(tablero)):
        return 5
    elif(empate(tablero)):
        return 0
    else:
        return -1
# Función que devuelve True o False si es ganador el jugador 1
def ganadorJug1(tablero):
    l1 = sum(tablero[0])
    l2 = sum(tablero[1])
    l3 = sum(tablero[2])
    c1 = sum(columna(0, tablero))
    c2 = sum(columna(1, tablero))
    c3 = sum(columna(0, tablero))
    d1 = sum([tablero[0][0], tablero[1][1], tablero[2][2]])
    d2 = sum([tablero[0][2], tablero[1][1], tablero[2][0]])

    return (l1 == 3) or (l2 == 3) or (d2 == 3)

# Función que dado un tablero y una posición de columna devuelve una columna
def columna(n, tablero):
    return [tablero[0][n], tablero[1][n], tablero[2][n]]
