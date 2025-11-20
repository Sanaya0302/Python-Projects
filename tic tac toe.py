the_board={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
board_keys=[]
for i in the_board:
    board_keys.append(i)
def print_board(board):
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print("-+-+-")
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print("-+-+-")
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print("-+-+-")
def game():
    turn="X"
    count=0
    for i in range(10):
        print_board(the_board)
        print("its your turn"+turn+"move to which place")
        move=input()
        if the_board[move]==" ":
            the_board[move]=turn
            count=count+1
        else:
            print("put it somewhere else!!!!!!!!")
            continue
        if count>=5:
            if the_board['1']==the_board['2']==the_board['3']!=' ':
                print_board(the_board)
                print("game over")
                print('****'+turn+'won****')
                break
            elif the_board['4']==the_board['5']==the_board['6']!=' ':
                print_board(the_board)
                print("game over")
                print('****'+turn+'won****')
                break
            elif the_board['7']==the_board['8']==the_board['9']!=' ':
                print_board(the_board)
                print("game over")
                print('****'+turn+'won****')
                break
            elif the_board['1']==the_board['4']==the_board['7']!=' ':
                print_board(the_board)
                print("game over")
                print('****'+turn+'won****')
                break
            elif the_board['2']==the_board['5']==the_board['8']!=' ':
                print_board(the_board)
                print("game over")
                print('****'+turn+'won****')
                break
            elif the_board['3']==the_board['6']==the_board['9']!=' ':
                print_board(the_board)
                print("game over")
                print('****'+turn+'won****')
                break
            elif the_board['1']==the_board['5']==the_board['9']!=' ':
                print_board(the_board)
                print("game over")
                print('****'+turn+'won****')
                break
            elif the_board['3']==the_board['5']==the_board['7']!=' ':
                print_board(the_board)
                print("game over")
                print('****'+turn+'won****')
                break
        if count==9:
            print("Game over!!!!!!!!!!!!!!")
            print("Its a tie!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            break
        if turn=="X":
            turn="O"
        else:
            turn="X"
    playagain=input("do you want to play again?(y/n)")
    if playagain=="y" or playagain=="Y":
        for key in board_keys:
            the_board[key]=' '
    else:
            print("bye bye!!!!!!!!!!!!!!!!!!!")
game()
if __name__=="__main__":
    game()