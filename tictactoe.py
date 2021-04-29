import IPython
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
def player_input():
    marker=''
    while not(marker=='x' or marker=='0'):
        marker=input('player 1: choose x or 0').upper()
    if marker=='x':
        return('x','0')
    else:
        return('0','x')
def place_marker(board,marker,position):
    board[position]=marker
def win_check(board,mark):
    return((board[7]==board[8]==board[9]==mark)or
           (board[4]==board[5]==board[6]==mark)or
           (board[1]==board[2]==board[3]==mark)or
           (board[1]==board[4]==board[7]==mark)or
           (board[2]==board[5]==board[8]==mark)or
           (board[3]==board[6]==board[9]==mark)or
           (board[1]==board[5]==board[9]==mark)or
           (board[3]==board[5]==board[7]==mark))
    
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board,position):
    return board[position]==' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('choose a position(1-9)'))
        return position
def replay():
    c=input("play again? Enter yes or No")
    return c=='yes'
print('WElCOME TO TIC TAC TOE')
while True:
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn + 'will go first')
    play_game=input('ready to play? y or n' )
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='player1':
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player1 has won')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    game_on=False
                else:
                    turn='player2'
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('player2 has won')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME')
                    game_on=False
                else:
                    turn='player1'
            
    if not replay():
        break
    

    
    
    
    
    
