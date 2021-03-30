"""
COMP.CS.100 Laivanupotus
Tekijä: Joose Lohi
Opiskelijanumero: 050800360

This program simulates the game known as 'Battleship'.
The input file determines the coordinates of the ships
and the player takes shots at the 10x10 board with coordinates
labeled XY, X in the range A-J and Y in 0-9.

The game ends either by the user entering 'q'/'Q' or
once all boats have been sunk.
"""


class Boat:
    """
    This class represents a boat in the game.
    The boat has the properties:
        name
        z (first letter)
        xy-coordinates
    """

    def __init__(self, name, z, coords):
        """
        :param name: str
        :param z: initial
        :param coords: list of coords
        """
        self.name = name
        self.z = z
        self.coords = coords

    def get_coords(self):
        """
        Get the list of coordinates of the boat.
        """
        return self.coords


def check_coords(boat_coords):
    """
    Check that all coordinates are
    in the following form:
        'XY'
        > X in 'ABCDEFGHIJ'
        > Y in '0123456789'
    return True/False to determine if program carries on
    """
    for xy in boat_coords:

        error = 'Error in ship coordinates!'

        # check for overlapping coordinates
        if boat_coords.count(xy) > 1:
            print('There are overlapping ships in the input file!')
            return False

        # coordinate out of range 'A12' or 'AB2'
        elif len(xy) != 2:
            print(error)
            return False

        elif xy[0] not in X:
            print(error)
            return False

        elif xy[1] not in Y:
            print(error)
            return False

    return True


def create_board():
    """
    Creat dictionary of all rows on the game board
    return {'row_x': '          '}
             name     0123456789
    """
    #  create a dict of all rows on board
    board = {}

    for i in range(0, 10):

        board[f'row_{i}'] = ' ' * 10

    return board


def print_board(board):
    """
    Printout the game board in the form:
    ROWS: 0-9
    COLUMNS: A-J
    """

    print()
    print(f'  {" ".join(X)}  ')
    i = 0

    for x in board:

        print(f'{i} {" ".join(board[x])} {i}')
        i += 1

    print(f'  {" ".join(X)}  ')


def alter_row(xy, s, board):
    """
    Change the value of the position the shot was taken.
    A: '          '  > shoot A3 > A: '   X      '

    :param xy: shot
    :param s: '*', 'X' or initial
    :param board: dictionary of all rows
    """
    row = board[f'row_{xy[1]}']
    index = X.index(xy[0])  # where the shot was taken within row
    row = row[:index] + s + row[index+1:]

    return row


def execute_command(xy, board, boat_coords, shots, boats):
    """
    React to the user prompt xy.
    'q' | 'Q'  ->  quit program
    bad input  ->  let user know
    good input ->  execute accordingly
    return True/False to determine if program runs
    """

    # quit
    if xy.upper() == 'Q':

        print('Aborting game!')
        return False

    # look for errors in prompt
    elif xy == "":
        print('Invalid command!')

    elif len(xy) != 2:
        print('Invalid command!')

    elif xy[0].upper() in X:
        if xy[1] in Y:

            # correct form 'a1' -> 'A1'
            xy = f'{xy[0].upper()}{xy[1]}'

            # valid shot
            if xy not in shots:

                shots.append(xy)
                shoot(board, boat_coords, xy, shots, boats)

            # shot already taken
            elif xy in shots:

                print('Location has already been shot at!')
        else:
            print('Invalid command')
    else:
        print('Invalid command!')

    return True


def shoot(board, boat_coords, xy, shots, boats):
    """
    Check if shot hits target and perform
    appropriate executions.
    :param board: game board
    :param boat_coords: coords of boats
    :param xy: shot
    :param shots: list of shots taken
    :param boats: dict of boat instances
    """

    #  check if shot hits boat -> 'X'
    if xy in boat_coords:

        #  alter the row
        board[f'row_{xy[1]}'] = alter_row(xy, 'X', board)

        #  assing variable to boat
        #  if shot in boat's coords
        for b in boats:
            if xy in boats[b].get_coords():
                boat = boats[b]

                    # if all coords of a boat are in
                    # shots, boat is not alive: 'XXX'  ->  'ZZZ'
                if all(coords in shots for coords in boat.get_coords()):

                    for coord in boat.coords:
                        board[f'row_{coord[1]}'] = alter_row(coord, boat.z, board)

                    # let the player know the boat is sank
                    print(f'You sank a {boat.name}!')

                else:
                    pass

            else:
                pass



    #  shot doesn't hit boat -> '*'
    else:
        board[f'row_{xy[1]}'] = alter_row(xy, '*', board)


# xy-coordinates
X = []
Y = []


# 'ABCDEFGHIJ'
for char in 'ABCDEFGHIJ':
    X.append(char)

# '0123456789'
for n in range(0, 10):
    Y.append(str(n))


def main():

    filename = input('Enter file name: ')

    # errors in opening file
    try:
        file = open(filename, mode='r')

    except OSError:
        print('File can not be read!')
        return


    #  create dictionary with name and boat object
    #  {'name_n': <object class=Boat>}
    boats = {}

    for row in file:  # get data from file

        i = 1
        row = row.rstrip().split(';')  # ['name', 'XY', 'XY']
        name = row[0]
        row.remove(row[0])  # ['XY', 'XY']

        #  if 'name_1' is taken,
        #  name = 'name_2' and so on..
        for boat in boats:
            if set(name).issubset(boat):
                i += 1
            else:
                pass

        boats[f'{name}_{i}'] = Boat(name, name[0].upper(), row)


    #  create list of all coordinates with boats
    boat_coords = []
    for b in boats:
        for xy in boats[b].coords:
            boat_coords.append(xy)


    #  check for errors in coordinates
    if check_coords(boat_coords):
        pass

    else:
        return  # break function if error found


    #  create a dict of all rows on board
    board = create_board()

    # list of shots taken
    shots = []

    #  initialize event loop
    while True:

        print_board(board)

        # if all boats are sank -> break loop
        if all(coords in shots for coords in boat_coords):
            print('\nCongratulations! You sank all enemy ships.')
            break

        # prompt player
        xy = input('\nEnter place to shoot (q to quit): ')

        # react to input
        if execute_command(xy, board, boat_coords, shots, boats):
            pass

        else:
            break


if __name__ == '__main__':
    main()
