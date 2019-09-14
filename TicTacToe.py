def start_game():
    '''
    This function works at the very beginning to welcome the players.
    It helps the player to understand how they play.
    It works also if the game restart
    :return:
    '''
    print("WELCOME TO TIC TAC TOE!!")
    print("THIS GAME IS PLAYED WITH NUMPAD..")
    player1 = 'a'
    player2 = 'a'

    while player1.lower() != 'x' and player1.lower() != 'o':
        player1 = input("Choose your side X or O :")
    if player1.lower() == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    print("Player1 : ",player1.upper())
    print("Player2 : ", player2.upper())
    return player1, player2

def draw_board(table):
    '''
    draw_board(table) draws the board to the screen.
    This function uses the table that is included X, O or spaces.
    :return:
    '''
    print("----------------")
    print("%3s | %3s | %3s "%(table[0][0], table[0][1], table[0][2]))
    print("----------------")
    print("%3s | %3s | %3s "%(table[1][0], table[1][1], table[1][2]))
    print("----------------")
    print("%3s | %3s | %3s "%(table[2][0], table[2][1], table[2][2]))
    print("----------------")

def ask_location(player, table):
    '''
    ask_location(player, table) asks the player about the place of his/her X/O.
    If the player choose somewhere is already chosen, it wants somewehere else.
    This function checks also whether the input is valid or not

    :param player:
    :param table:
    :return:
    '''
    d = {'7':table[0][0], '8': table[0][1], '9':table[0][2], '4': table[1][0], '5': table[1][1], '6': table[1][2], '1': table[2][0], '2': table[2][1], '3': table[2][2]}
    player_location = input("Location of {} :".format(player.upper()))
    while d[player_location] != '' or not player_location in '123456789':
        player_location = input("Location of {} :".format(player.upper()))

    if player_location == '7':
        table[0][0] = player
    if player_location == '8':
        table[0][1] = player
    if player_location == '9':
        table[0][2] = player
    if player_location == '4':
        table[1][0] = player
    if player_location == '5':
        table[1][1] = player
    if player_location == '6':
        table[1][2] = player
    if player_location == '1':
        table[2][0] = player
    if player_location == '2':
        table[2][1] = player
    if player_location == '3':
        table[2][2] = player
    return table

def check_winner(table):
    '''
    check_winner(table) hellps us to decide who won or whether it is tie.
    Check row by row, column by column and the crosses.
    It also checks if there is no spaces, if so, it is a tie.

    :param table:
    :return:
    '''
    count = 0
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != '':
            return table[i][0]
        if table[0][i] == table[1][i] == table[2][i] != '':
            return table[0][i]
        count += table[i].count('')
    if table[0][0] == table[1][1] == table[2][2] != '':
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] != '':
        return table[1][1]
    if count == 0:
        return 'T'
    return 1

def game_play(player, table):
    '''
    This function calls the functions step by step in order to players play.

    :param player:
    :param table:
    :return:
    '''

    state = check_winner(table)

    if state == player:
        draw_board(table)
        print("{} wins..".format(player))
    if state == 'T':
        draw_board(table)
        print("It's tie..")
    if state == player or state == 'T':
        replay = input("One more time : [y/N]\t")
        if replay.lower() == "y":
            return True
        else:
            print("Goodbye..")
            exit()
    return False

#GAME STARTS NOW :)

restart = True

while True:
    if restart:
        mat = [['', '', ''], ['', '', ''], ['', '', '']]
        player1, player2 = start_game()
        restart = False

    draw_board(mat)
    mat = ask_location(player1, mat)

    restart = game_play(player1, mat)

    if not restart:
        draw_board(mat)
        mat = ask_location(player2, mat)
        restart = game_play(player2, mat)