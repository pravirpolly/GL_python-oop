__author__ = 'Endri Dani'

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_status = False


def board():
    print " {} | {} | {}\n {} | {} | {}\n {} | {} | {}".format(*matrix)


def reset_board():
    global matrix, game_status
    matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_status = False


def select_position():
    global marker, position, item
    marker = ''
    position = ''
    while not (marker == 'x' or marker == 'o' or position in range(1, 10)):
        marker, position = raw_input("\n Enter the player's marker and the position you want:").split()
    for number in matrix:
        item = matrix.index(number)
        if int(position) == matrix[item]:
            matrix[item] = marker
            board()


def check_status():
    global game_status
    if matrix[0] == matrix[1] == matrix[2] == marker or matrix[3] == matrix[4] == matrix[5] == marker or matrix[6] == \
            matrix[7] == matrix[7] == marker or matrix[0] == matrix[3] == matrix[6] == marker or matrix[1] == matrix[
        4] == matrix[7] == marker or matrix[2] == matrix[5] == matrix[8] == marker or matrix[0] == matrix[4] == matrix[
        8] == marker or matrix[2] == matrix[4] == matrix[6] == marker:
        print "\n {player} Wins! Congratulations!".format(player=marker)
        game_status = True
    elif all(isinstance(x, str) for x in matrix) and game_status is False:
            print "\n The game is draw!"


def play_game():
    reset_board()
    board()
    while any(not isinstance(x, str) for x in matrix) and game_status is False:
        select_position()
        check_status()
    rematch = raw_input('Would you like to play again? (y/n):')
    if rematch == 'y':
        play_game()
    else:
        print "Thanks for playing!"

play_game()

