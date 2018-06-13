import sys



board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fine = False
turno = True
mosse = 0
win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

giocatore1 = input("giocatore numero1, nome:\n ")
giocatore2 = input("giocatore numero2, nome:\n ")
print("giocatore numero1 il tuo nome è: \t" + giocatore1 + "\t e il tuo simbolo è: O \n" + "giocatore numero2 il tuo nome è: \t" + giocatore2 + "\t e il tuo simbolo è: X")


def tabella():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print()


def controllo(a):
    while True:
        try:
            a = int(a)
            a = a - 1
            if a in range(0, 9):
                return a
            else:
                print("\nnon è sulla tabella. riprova:")
                return None

        except ValueError:
            print("\nNon è un numero riprova:")
            return None


def player1(mosse):
    global board
    a = input("numero: ")
    oknumber=controllo(a)
    if oknumber is not None:
        if board[oknumber] == "X" or board[oknumber] == "O":
            print("\ncasella già occupata. riprova")
            player1(mosse)
        else:
            board[oknumber] = "O"
            return mosse
    player1(mosse)


def player2(mosse):
    global board
    a = input("numero: ")
    oknumber=controllo(a)
    if oknumber is not None:
        if board[oknumber] == "X" or board[oknumber] == "O":
            print("\ncasella già occupata. riprova")
            player2(mosse)
        else:
            board[oknumber] = "X"
            return mosse
    player2(mosse)


def cambioTurno(mosse):
    t =  mosse % 2
    if t==0 :
        turno = True
    else:
        turno = False

    return turno

def check_board():
    count = 0
    for oknumber in win_commbinations:
        if board[oknumber[0]] == board[oknumber[1]] == board[oknumber[2]] == "X":
            print(giocatore1+" vince!\n")
            return True
        if board[oknumber[0]] == board[oknumber[1]] == board[oknumber[2]] == "O":
            print(giocatore2+" vince!\n")
            return True
    for oknumber in range(9):
        if board[oknumber] == "X" or board[oknumber] == "O":
            count += 1
        if count == 9:
            print("il gioco finisce in parità\n")
            return True


def main(args=None):
    global fine
    global mosse
    while not fine:
        commutaPlayer = cambioTurno(mosse)
        if commutaPlayer == True:
            tabella()
            print(giocatore1 + " è il tuo turno. dove vuoi mettere il tuo segno:\n")
            player1(mosse)
            mosse = mosse + 1
            fine = check_board()
        else:
            tabella()
            print(giocatore2 + " è il tuo turno. dove vuoi mettere il tuo segno:\n")
            player2(mosse)
            mosse = mosse + 1
            fine = check_board()


if __name__ == '__main__':
    main(sys.argv[1:])
