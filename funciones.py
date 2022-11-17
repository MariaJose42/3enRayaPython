import os

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
    os.system ("clear")
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
    if(pos == "a0"):
        tablero[0][0] = jug
    elif(pos == "a1"):
        tablero[0][1] = jug
    elif(pos == "a2"):
        tablero[0][2] = jug
    elif(pos == "b0"):
        tablero[1][0] = jug
    elif(pos == "b1"):
        tablero[1][1] = jug
    elif(pos == "b2"):
        tablero[1][2] = jug
    elif(pos == "c0"):
        tablero[2][0] = jug
    elif(pos == "c1"):
        tablero[2][1] = jug
    elif(pos == "c2"):
        tablero[2][2] = jug

# Devuelve True o False si hay una pieza en la posición
def hayPieza(pos, tablero):
    if(pos == "a0"):
        return tablero[0][0] != 0
    elif(pos == "a1"):
        return tablero[0][1] != 0
    elif(pos == "a2"):
        return tablero[0][2] != 0
    elif(pos == "b0"):
        return tablero[1][0] != 0
    elif(pos == "b1"):
        return tablero[1][1] != 0
    elif(pos == "b2"):
        return tablero[1][2] != 0
    elif(pos == "c0"):
        return tablero[2][0] != 0
    elif(pos == "c1"):
        return tablero[2][1] != 0
    elif(pos == "c2"):
        return tablero[2][2] != 0
    else:
        #print(pos, "no es una coordenada valida.")
        return True

def empate(tablero):
    if(not ganadorJug2(tablero) or not ganadorJug1(tablero)):
        if((0 in tablero[0]) or (0 in tablero[1]) or (0 in tablero[2])):
            return False
        else:
            return True
    else:
        return False

def juega(jugador_actual, tablero):
        if(jugador_actual == 1):
            print("Juega el jugador 1 (X)")
        else:
            print("Juega el jugador 2 (O)")
        pos = input("Dime coordenada: ")
        if(not hayPieza(pos, tablero)):
            colocarPieza(jugador_actual, pos, tablero)
            
            if(jugador_actual == 1):
                return 5
            else:
                return 1
            
        else:
            print("Hay una pieza prueba otra coordenada")
            return jugador_actual



