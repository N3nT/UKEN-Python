import random

def set_ship():
    ships = set()

    for i in range(5):
        ship = (random.randint(0,9), random.randint(0,9))
        ships.add(ship)

    return ships

def print_board(board):
    for tab in board:
        print(tab)

def game():
    ships = set_ship()
    board = [["." for _ in range(10)] for _ in range(10)]
    moves = 0
    shooted = 0
    while True:
        print_board(board)
        odp_x = int(input("Podaj wspolrzena x: "))
        odp_y = int(input("Podaj wspolrzena x: "))
        tries = (odp_x, odp_y)

        if tries in ships:
            board[odp_x][odp_y] = "X"
            shooted += 1
        else:
            board[odp_x][odp_y] = "O"

        moves += 1
        if shooted == 5:
            print(f"Wygrales w {moves} ruchach")
            break

game()




