def printBoard(gameValues):
    print(f"{gameValues[0]} | {gameValues[1]} | {gameValues[2]}")
    print(f"--|---|--")
    print(f"{gameValues[3]} | {gameValues[4]} | {gameValues[5]}")
    print(f"--|---|--")
    print(f"{gameValues[6]} | {gameValues[7]} | {gameValues[8]}")


def checkWin(gameValues):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'X':
            printBoard(gameValues)
            print("X won the match")
            return 1
        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'O':
            printBoard(gameValues)
            print("0 won the match")
            return 0
        if all(isinstance(item, str) for item in gameValues):
            printBoard(gameValues)
            return -2
    return -1


if __name__ == '__main__':
    gameValues = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    turn = 1  # 1 for X and 0 for O
    print("Wellcome to Tic-Tac-Toe")

    while True:

        if turn == 1:
            printBoard(gameValues)
            print("X's chance- ")
            value = int(input("Please enter a value: "))

            if gameValues[value] != 'O':
                gameValues[value] = 'X'
            else:
                continue

        else:
            printBoard(gameValues)
            print("O's chance- ")
            value = int(input("Please enter a value: "))

            if gameValues[value] != 'X':
                gameValues[value] = 'O'
            else:
                continue

        turn = 1 - turn
        cwin = checkWin(gameValues)

        if cwin == -2:
            print("Game Draw")
            break
        if cwin != -1:
            print("Match over ")
            break
