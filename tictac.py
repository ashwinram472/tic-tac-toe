###############################
##### TIC TAC TOE #############
##### ASHWIN BALASUBRAMANIAM ##
###############################

# Setting the Grid
def set_grid():
    global grid
    grid = [['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3']]

# Printing the GRID


def print_grid():
    for i in range(3):
        print(*grid[i])
    print('____________________________________')
    print(' ')

# Checking the Match


def game_check(player):
    # Inputting the X, O
    grid[loc[0]][loc[1]] = player
    print_grid()
    # horizontal check
    for i in range(3):
        if len(set(grid[i])) == 1:
            print('Horizontal match')
            return True
    # vertical check
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] == player:
            print('Vertical Match')
            return True
    # cross check
    for i in [0, 2]:
        if i == 0 and (grid[i][i] == grid[i+1][i+1] == grid[i+2][i+2] == player):
            print('Cross Match')
            return True
        if i == 2 and (grid[i-2][i] == grid[i-1][i-1] == grid[i][i-2] == player):
            print('Cross Match')
            return True
    return False


# Dictionary holding the locations of the list
d = {'A1': [0, 0], 'A2': [1, 0], 'A3': [2, 0], 'B1': [0, 1], 'B2': [
    1, 1], 'B3': [2, 1], 'C1': [0, 2], 'C2': [1, 2], 'C3': [2, 2]}

# Checking for the correct input


def check_grid():
    position = input("Choose Position:").upper()
    # Checking if the input is outisde the grid
    if position not in [*d]:
        print('Enter the location in the grid')
        l = check_grid()
        return l
    else:
        # Checking if the input is overlapping
        l = d[position]
        if (grid[l[0]][l[1]] in ['X', 'O']):
            print('Cannot overlap. Enter another location')
            l = check_grid()
            return l
        elif position in [*d]:
            return d[position]

# Alternating the players , Getting input and checking the game


def game():
    print_grid()
    global loc
    for i in range(9):
        loc = check_grid()
        if i % 2 == 0:
            c = game_check('X')
            if c:
                print('Player 1 won')
                print_grid()
                exit()
            elif i == 8:
                print(' Its a tie')
                print_grid()
                exit()
        elif i % 2 == 1:
            c = game_check('O')
            if c:
                print('Player 2 won')
                print_grid()
                exit()


# Main function
if __name__ == '__main__':
    val = True
    set_grid()
    print('Starting the game')
    game()
