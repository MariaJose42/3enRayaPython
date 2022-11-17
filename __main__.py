import funciones

def main():
    jugador_actual = 1
    tablero = funciones.inicializarTablero()
    
    while(True):
        if(funciones.esGanador(tablero) == 1):
            #Gana el jugador 1
            print("GANA EL JUGADOR 1 (X)")
            break
        elif(funciones.esGanador(tablero) == 5):
            #Gana el jugador 2
             print("GANA EL JUGADOR 2 (O)")
             break
        elif(funciones.esGanador(tablero) == 0):
            #Empate
             print("EMPATE")
             break
        else:
            #Se esta jugando
            funciones.pintarTablero(tablero)
            jugador_actual = funciones.juega(jugador_actual, tablero)
            
#comienza el juego
main()
