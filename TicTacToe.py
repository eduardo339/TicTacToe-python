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
    gameMain()

def gameMain():
    SIZE = 9
    currentState = State.PLAYING
    currentPlayer = Seed.CROSS.value
    #Tablero
    cells = [''] * SIZE
    
    muestra(SIZE)
    newGame(cells, SIZE, currentPlayer, currentState)

    while currentState == State.PLAYING:
        stepGame(cells, currentPlayer, currentState)
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
    
def stepGame(cells, currentPlayer, currentState):
    flag = True
    while flag:
        tiro = int(input('{} ingresa un movimiento [1-9]:'.format(currentPlayer)))
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
            if(cells[i] == Seed.NO_SEED.value):
                return State.PLAYING
    return State.DRAW

main()