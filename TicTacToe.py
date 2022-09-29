import enum
class State(enum.Enum):
    PLAYING = 1
    CROSS_WON = 2
    NOUGHT_WON = 3
    DRAW = 0

class Seed(enum.Enum):
    CROSS = 'X'
    NOUGTH = 'O'
    NO_SEED = ' '

#Metodo main
def main():

    while True:
        gameMain()
        again = int(input('Quieres volver a jugar?\n1.-SI\n2.-NO\n'))
        if again == 1:
            pass
        else:
            print('ADIOS :D')
            break

def gameMain():
    SIZE = 9
    currentState = State.PLAYING
    currentPlayer = Seed.CROSS.value
    go = 0
    #Tablero
    cells = [''] * SIZE
    turno = 1
    muestra(SIZE)
    newGame(cells, SIZE, currentPlayer, currentState)

    while True:
        go = int(input('Selecciona tu jugador.\n1.-PLAYER 1\n2.-PLAYER 2\n'))
        if go == 1 or go == 2:
            break
        else: 
            print('Ese jugador no es una opcion valida.')

    while currentState == State.PLAYING:
        stepGame(cells, currentPlayer,turno,SIZE, go)
        turno = turno + 1
        Board(cells)
        #Verifica si el estado del juego     
        if posWin(cells,SIZE,currentPlayer,currentState) == State.CROSS_WON:
            print('Ganaron las {} Adios'.format(currentPlayer))
            break
        elif posWin(cells,SIZE,currentPlayer,currentState) == State.NOUGHT_WON:
            print('Ganaron las {} Adios'.format(currentPlayer))
            break
        elif posWin(cells,SIZE,currentPlayer,currentState) == State.DRAW:
            print('Fue empate Adios')
            break        
        #Cambio de jugador
        currentPlayer = Seed.NOUGTH.value if (currentPlayer == Seed.CROSS.value) else Seed.CROSS.value

def Board(cells):
    print()
    print()
    # va del 0 - 8 y salta de 3 en 3
    for i in range(0, 8, 3):
        #imprime una linea vertical para el tablero
        print('             {}'.format(cells[i]) + '|' + '{}'.format(cells[i+1]) + '|' + '{}'.format(cells[i+2]))
        if(i < 5): #imprime una linea horizontal para el tablerp
            print('             -----')
    print()
    print()

def newGame(cells, SIZE, currentPlayer, currentState):
    #LLenado de tablero
    paint(cells, SIZE, True)
    currentPlayer = Seed.CROSS.value
    currentState = State.PLAYING
    
def stepGame(cells, currentPlayer, turno, size, go):
        #JUGADOR empieza
        if go == 1:
            if(currentPlayer == Seed.CROSS.value):
                flag = True
                while flag:
                    tiro = int(input('Turno de las {}. Ingresa un movimiento [1-9]:'.format(currentPlayer)))
                    if tiro > 0 and tiro <= 9 and cells[tiro - 1] == Seed.NO_SEED.value:
                        cells[tiro - 1] = currentPlayer
                        flag = False
                    else:
                        print('El movimiento en {} no es una jugada valida. Intenta otra vez...'.format(tiro))
            else:
                MoveIA(cells , turno, currentPlayer, size, go)
            loop = False
        #MAQUINA empieza
        elif go == 2:
            if(currentPlayer == Seed.CROSS.value):
                MoveIA(cells , turno, currentPlayer,size, go)
            else:
                flag = True
                while flag:
                    tiro = int(input('Turno de las {}. Ingresa un movimiento [1-9]:'.format(currentPlayer)))
                    if tiro > 0 and tiro <= 9 and cells[tiro - 1] == Seed.NO_SEED.value:
                        cells[tiro - 1] = currentPlayer
                        flag = False
                    else:
                        print('El movimiento en {} no es una jugada valida. Intenta otra vez...'.format(tiro))


def muestra(size):
    arrMuestra = [''] * size
    paint(arrMuestra,size,False)
    #impresion del Tablero
    print()
    print('#################################')
    print('       *Tablero TicTacToe*')
    # va del 0 - 8 y salta de 3 en 3
    for i in range(0, 8, 3):
        #imprime una linea vertical para el tablero
        print('             {}'.format(arrMuestra[i]) + '|' + '{}'.format(arrMuestra[i+1]) + '|' + '{}'.format(arrMuestra[i+2]))
        if(i < 5): #imprime una linea horizontal para el tablerp
            print('             -----')
    print('#################################')

def paint(cells, size, inPaint):
    if(inPaint):    
        for i in range(size):
            cells[i] = Seed.NO_SEED.value
    else:
        for i in range(size):
            cells[i] = i + 1

def posWin(cells,size,currentPlayer,currentState):
    #3 en linea, 3 en fila y cruzado
    if cells[0] == currentPlayer and cells[1] == currentPlayer and cells[2] == currentPlayer or \
    cells[3] == currentPlayer and cells[4] == currentPlayer and cells[5] == currentPlayer or \
    cells[6] == currentPlayer and cells[7] == currentPlayer and cells[8] == currentPlayer or \
    cells[0] == currentPlayer and cells[3] == currentPlayer and cells[6] == currentPlayer or \
    cells[1] == currentPlayer and cells[4] == currentPlayer and cells[7] == currentPlayer or \
    cells[2] == currentPlayer and cells[5] == currentPlayer and cells[8] == currentPlayer or \
    cells[0] == currentPlayer and cells[4] == currentPlayer and cells[8] == currentPlayer or \
    cells[6] == currentPlayer and cells[4] == currentPlayer and cells[2] == currentPlayer:
        return  State.CROSS_WON if(currentPlayer == Seed.CROSS.value) else State.NOUGHT_WON
    else:
        for i in range(size):
            if cells[i] == Seed.NO_SEED.value:
                return State.PLAYING
    return State.DRAW

def MoveIA(cells, turno, currentPlayer, size, go):
    print('Turno de las {}. Tira en:'.format(currentPlayer))
    if go == 1:
        IAPlayer2(turno, cells, currentPlayer,size)
    else:
        IAPlayer1(turno, cells, currentPlayer,size)

def IAPlayer1(turno, cells, currentPlayer,size):    
    if turno == 1:
        cells[0] = currentPlayer
    elif turno== 3:
        if cells[4] == Seed.NO_SEED.value:
            cells[4] = currentPlayer
        elif cells[8] == Seed.NO_SEED.value:
            cells[8] = currentPlayer
        else:
            cells[2] = currentPlayer
    elif turno == 5:
        MovesP1(cells, currentPlayer)
    elif turno == 7:
        MovesP1(cells, currentPlayer)
    elif turno == 9:
        for i in range(size):
            if(cells[i] == Seed.NO_SEED.value):
                cells[i] = currentPlayer

def MovesP1(cells, currentPlayer):
    #CROSS
    if cells[0] == cells[2] == Seed.CROSS.value and cells[1] == Seed.NO_SEED.value: #[0][0] - [0][2] ---> [0][1]
        cells[1] = currentPlayer
    elif cells[2] ==  cells[8] == Seed.CROSS.value and cells[5] == Seed.NO_SEED.value:   #[0][2] - [2][2] ---> [1][2]
        cells[5] = currentPlayer
    elif cells[8] ==  cells[6] == Seed.CROSS.value and cells[7] == Seed.NO_SEED.value: #[2][2] - [2][0] ---> [2][1]
        cells[7] = currentPlayer
    elif cells[7] ==  cells[4] == Seed.CROSS.value and cells[1] == Seed.NO_SEED.value: #[2][1] - [1][1] ---> [0][1]
        cells[1] = currentPlayer
    elif cells[4] ==  cells[5] == Seed.CROSS.value and cells[3] == Seed.NO_SEED.value: #[1][1] - [1][2] ---> [1][0]
        cells[3] = currentPlayer
    elif cells[0] ==  cells[6] == Seed.CROSS.value and cells[3] == Seed.NO_SEED.value: #[0][0] - [2][0] ---> [1][0]
        cells[3] = currentPlayer
    elif cells[0] ==  cells[4] == Seed.CROSS.value and cells[8] == Seed.NO_SEED.value: #[0][0] - [2][0] ---> [1][0]
        cells[8] = currentPlayer
    #NOUGHT
    elif cells[4] ==  cells[1] == Seed.NOUGTH.value and cells[7] == Seed.NO_SEED.value: #[1][1] - [0][1] ---> [2][1]
        cells[7] = currentPlayer
    elif cells[4] ==  cells[3] == Seed.NOUGTH.value and cells[5] == Seed.NO_SEED.value: #[1][1] - [1][0] ---> [1][2]
        cells[5] = currentPlayer
    elif cells[4] ==  cells[7] == Seed.NOUGTH.value and cells[1] == Seed.NO_SEED.value: #[1][1] - [2][1] ---> [0][1]
        cells[1] = currentPlayer
    elif cells[4] ==  cells[5] == Seed.NOUGTH.value and cells[3] == Seed.NO_SEED.value: #[1][1] - [1][2] ---> [1][0]
        cells[3] = currentPlayer
    elif cells[4] ==  cells[2] == Seed.NOUGTH.value and cells[6] == Seed.NO_SEED.value: #[1][1] - [0][2] ---> [2][0]
        cells[6] = currentPlayer
    elif cells[4] ==  cells[6] == Seed.NOUGTH.value and cells[2] == Seed.NO_SEED.value: #[1][1] - [2][0] ---> [0][2]
        cells[2] = currentPlayer
        
    elif cells[2] ==  cells[8] == Seed.NOUGTH.value and cells[5] == Seed.NO_SEED.value: #[0][2] - [2][2] ---> [1][2]
        cells[5] = currentPlayer
    elif cells[8] ==  cells[6] == Seed.NOUGTH.value and cells[7] == Seed.NO_SEED.value: #[2][2] - [2][0] ---> [2][1]
        cells[7] = currentPlayer
    elif cells[2] ==  cells[8] == Seed.CROSS.value and cells[5] == Seed.NO_SEED.value: #[0][2] - [2][2] ---> [1][2]
        cells[5] = currentPlayer
    elif cells[8] ==  cells[6] == Seed.CROSS.value and cells[7] == Seed.NO_SEED.value: #[2][2] - [2][0] ---> [2][1]
        cells[7] = currentPlayer
    #Tiro faltante    
    elif cells[2] == Seed.NO_SEED.value: #[0][2] ----> [0][2]
        cells[2] = currentPlayer
    elif cells[5] == Seed.NO_SEED.value: #[1][2] ----> [1][2]
        cells[5] = currentPlayer
    elif cells[7] == Seed.NO_SEED.value: #[2][1] ----> [2][1]
        cells[7] = currentPlayer
    elif cells[6] == Seed.NO_SEED.value: #[2][0] ----> [2][0]
        cells[6] = currentPlayer

def IAPlayer2(turno, cells, currentPlayer,size):
    if turno == 2:
        if cells[4] == Seed.NO_SEED.value:
            cells[4] = currentPlayer
        else:
            cells[0] = currentPlayer
    elif turno == 4:
        MovesP2(cells, currentPlayer, turno)
    elif turno == 6:
        MovesP2(cells, currentPlayer, turno)
    elif turno == 8:
        MovesP2(cells, currentPlayer, turno)

def MovesP2(cells, currentPlayer,trn):
    winIA(cells, currentPlayer)
    if cells[0] == cells[2] == Seed.CROSS.value and cells[1] == Seed.NO_SEED.value:
        cells[1] = currentPlayer
    elif cells[2] == cells[8] == Seed.CROSS.value and cells[5] == Seed.NO_SEED.value:
        cells[5] = currentPlayer
    elif cells[0] == cells[6] == Seed.CROSS.value and cells[3] == Seed.NO_SEED.value:
        cells[3] = currentPlayer
    elif cells[6] == cells[8] == Seed.CROSS.value and cells[7] == Seed.NO_SEED.value:
        cells[7] = currentPlayer
    elif cells[4] ==  cells[1] == Seed.CROSS.value and cells[7] == Seed.NO_SEED.value: #[1][1] - [0][1] ---> [2][1]
        cells[7] = currentPlayer
    elif cells[4] ==  cells[3] == Seed.CROSS.value and cells[5] == Seed.NO_SEED.value: #[1][1] - [1][0] ---> [1][2]
        cells[5] = currentPlayer
    elif cells[4] ==  cells[7] == Seed.CROSS.value and cells[1] == Seed.NO_SEED.value: #[1][1] - [2][1] ---> [0][1]
        cells[1] = currentPlayer
    elif cells[4] ==  cells[5] == Seed.CROSS.value and cells[3] == Seed.NO_SEED.value: #[1][1] - [1][2] ---> [1][0]
        cells[3] = currentPlayer
    elif cells[4] ==  cells[2] == Seed.CROSS.value and cells[6] == Seed.NO_SEED.value: #[1][1] - [0][2] ---> [2][0]
        cells[6] = currentPlayer
    elif cells[4] ==  cells[6] == Seed.CROSS.value and cells[2] == Seed.NO_SEED.value: #[1][1] - [2][0] ---> [0][2]
        cells[2] = currentPlayer
    elif cells[8] ==  cells[7] == Seed.CROSS.value and cells[6] == Seed.NO_SEED.value: #[1][1] - [2][0] ---> [0][2]
        cells[6] = currentPlayer
    elif cells[6] ==  cells[7] == Seed.CROSS.value and cells[8] == Seed.NO_SEED.value: #[1][1] - [2][0] ---> [0][2]
        cells[8] = currentPlayer
    elif cells[0] == Seed.NO_SEED.value:
        cells[0] = currentPlayer
    elif cells[1] == Seed.NO_SEED.value:
        cells[1] = currentPlayer
    else:
        cells[7] = currentPlayer

def winIA(cells, currentPlayer):
    if cells[4] == cells[0] == Seed.NOUGTH.value and cells[8] == Seed.NO_SEED.value:
        cells[8] = currentPlayer
    elif cells[4] == cells[2] == Seed.NOUGTH.value and cells[6] == Seed.NO_SEED.value:
        cells[6] = currentPlayer
    elif cells[4] == cells[8] == Seed.NOUGTH.value and cells[0] == Seed.NO_SEED.value:
        cells[0] = currentPlayer
    elif cells[4] == cells[6] == Seed.NOUGTH.value and cells[2] == Seed.NO_SEED.value:
        cells[2] = currentPlayer
    elif cells[4] == cells[1] == Seed.NOUGTH.value and cells[7] == Seed.NO_SEED.value:
        cells[7] = currentPlayer
    elif cells[4] == cells[3] == Seed.NOUGTH.value and cells[5] == Seed.NO_SEED.value:
        cells[5] = currentPlayer
    elif cells[4] == cells[5] == Seed.NOUGTH.value and cells[3] == Seed.NO_SEED.value:
        cells[3] = currentPlayer
    elif cells[4] == cells[7] == Seed.NOUGTH.value and cells[1] == Seed.NO_SEED.value:
        cells[1] = currentPlayer
    elif cells[0] == cells[1] == Seed.NOUGTH.value and cells[2] == Seed.NO_SEED.value:
        cells[2] = currentPlayer
    elif cells[0] == cells[3] == Seed.NOUGTH.value and cells[6] == Seed.NO_SEED.value:
        cells[6] = currentPlayer
    elif cells[0] == cells[2] == Seed.NOUGTH.value and cells[1] == Seed.NO_SEED.value:
        cells[1] = currentPlayer
    elif cells[0] == cells[6] == Seed.NOUGTH.value and cells[3] == Seed.NO_SEED.value:
        cells[3] = currentPlayer
    elif cells[2] == cells[8] == Seed.NOUGTH.value and cells[5] == Seed.NO_SEED.value:
        cells[5] = currentPlayer
    elif cells[8] == cells[6] == Seed.NOUGTH.value and cells[7] == Seed.NO_SEED.value:
        cells[7] = currentPlayer
main()