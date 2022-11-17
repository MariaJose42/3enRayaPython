tp1 = [[1,1,0],[0,0,1],[5,5,0]]
tp2 = [[1,1,1],[0,5,1],[5,5,0]]
tp3 = [[1,0,0],[1,5,1],[1,5,0]]
tp4 = [[1,0,0],[5,1,1],[1,5,1]]
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
'''
Función que devuelve True or False si gana el Jugador 1
'''
def ganadorJug1(tablero):
    l1 = sum(tablero[0])
    l2 = sum(tablero[1])
    l3 = sum(tablero[2])
    c1 = sum(columna(0, tablero))
    c2 = sum(columna(1, tablero))
    c3 = sum(columna(2, tablero))
    d1 = sum([tablero[0][0], tablero[1][1], tablero[2][2]])
    d2 = sum([tablero[0][2], tablero[1][1], tablero[2][0]])

    return (l1 == 3) or (l2 == 3) or (l2 == 3) or (c1 == 3) or (c2==3) or (c3==3) or (d1 == 3) or (d2 ==3)
'''
Función que devuelve True or False si gana el Jugador 2
'''
def ganadorJug2(tablero):
    l1 = sum(tablero[0])
    l2 = sum(tablero[1])
    l3 = sum(tablero[2])
    c1 = sum(columna(0, tablero))
    c2 = sum(columna(1, tablero))
    c3 = sum(columna(2, tablero))
    d1 = sum([tablero[0][0], tablero[1][1], tablero[2][2]])
    d2 = sum([tablero[0][2], tablero[1][1], tablero[2][0]])

    return (l1 == 15) or (l2 == 15) or (l2 == 15) or (c1 == 15) or (c2==15) or (c3==15) or (d1 == 15) or (d2 == 15)


# Devuelve la columna n del tablero
def columna(n, tablero):
    return [tablero[0][n], tablero[1][n], tablero[2][n]]

# Devuelve True o False si ha colocado la pieza en la posción
def colocarPieza(jug, pos, tablero):
    pass
# Devuelve True o False si hay una pieza en la posición
def hayPieza(pos, tablero):
    pass

'''
# Devuelve True or False si es un estado del tablero en empate
def empate(tablero):
    res = ""

    l1 = sum(tablero[0])
    l2 = sum(tablero[1])
    l3 = sum(tablero[2])
    c1 = sum(columna(0, tablero))
    c2 = sum(columna(1, tablero))
    c3 = sum(columna(0, tablero))
    
    devolver = False

    if((l1 > 3) and (l2 > 3) and (l1 > 3)):
        res = "El juego se ha terminado - Empate"
        devolver = True
    
    return devolver
'''

def empate(tablero):
    if(not ganadorJug2(tablero) or not ganadorJug1(tablero)):
        if((0 in tablero[0]) or (0 in tablero[1]) or (0 in tablero[2])):
            return False
        else:
            return True
    else:
        return False


'''
1 --> Gana jugador 1
2 --> Gana jugado 2
0 --> Empate (FIN)
-1 --> Se esta jugando
'''
e1_tab = inicializarTablero()
e2_tab = [[1,0,5],[1,5,1],[1,0,0]]
e3_tab = [[1,0,5],[1,1,5],[0,0,1]]
e4_tab = [[1,0,5],[1,1,5],[0,0,5]]
e5_tab = [[5,5,5],[1,1,0],[0,0,1]]
e6_tab = [[5,1,5],[1,5,1],[1,0,0]]
print(esGanador(e6_tab))
