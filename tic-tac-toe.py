def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if oState[0] else 0)
    one = 'X' if xState[1] else ('O' if oState[1] else 1)
    two = 'X' if xState[2] else ('O' if oState[2] else 2)
    three = 'X' if xState[3] else ('O' if oState[3] else 3)
    four = 'X' if xState[4] else ('O' if oState[4] else 4)
    five = 'X' if xState[5] else ('O' if oState[5] else 5)
    six = 'X' if xState[6] else ('O' if oState[6] else 6)
    seven = 'X' if xState[7] else ('O' if oState[7] else 7)
    eight = 'X' if xState[8] else ('O' if oState[8] else 8)
    
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")
    
    
def winner(xState, oState):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical wins
        [0, 4, 8], [2, 4, 6]              # Diagonal wins
    ]
    for win in wins:
        if xState[win[0]] + xState[win[1]] + xState[win[2]] == 3:
            print("\n**********Winner: Player 1**********")
            return 1
        if oState[win[0]] + oState[win[1]] + oState[win[2]] == 3:
            print("\n**********Winner: Player 2**********")
            return 0
    return -1

print("**********TIC TAC TOE GAME**********\n")
while True:
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # turn for X first (0 for O)
    
    while True:
        printBoard(xState, oState)

        if turn == 1:
            print("\nPlayer 1's Chance")
            value = int(input("Enter the value: "))
            xState[value] = 1
        else:
            print("\nPlayer 2's Chance")
            value = int(input("Enter the value: "))
            oState[value] = 1

        w = winner(xState, oState)
        
        if w != -1:
            printBoard(xState,oState)
            print("\n**********Match Over**********")
            break

        # Draw condition
        if sum(xState) + sum(oState) == 9:
            printBoard(xState, oState)
            print("\n**********Draw**********")
            break

        turn = 1 - turn
        
    # Play again option
    play_again = input("Do you want to play again? (y/n): ")
    if play_again != "y":
        print("\n**********Thanks for playing**********")
        break