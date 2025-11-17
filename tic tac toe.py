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
        else:
            print("put it somewhere else!!!!!!!!")
            continue
