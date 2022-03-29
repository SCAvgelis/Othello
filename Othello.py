
def create_board ():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(0)
    board[3][3] = 1
    board[3][4] = 2
    board[4][3] = 2
    board[4][4] = 1
    return board

def print_board(board):
    for row in range(len(board)):
        print(*board[row], sep='')
    return

def replace_bottomup(board,x,y,color):
    posx = []
    i = 1
    if x < 0 and y < 0 and x > 7 and y > 7:
        return posx
    while True:
        if board[x-i][y] != color and board[x-i][y] != 0 and x-i >= 0:
            posx.append(x - i)
            i +=1
        else:
            break
    a = [posx, y]
    return a

def replace_topdown(board,x,y,color):
    posx = []
    i = 1
    if x < 0 and y < 0 and x > 7 and y > 7:
        return posx
    while True:
        if board[x+i][y] != color and board[x+i][y] != 0 and x+i <= 7:
            posx.append(x + i)
            i +=1
        else:
            break
    a = [posx, y]
    return a

def replace_leftright(board,x,y,color):
    posy = []
    i = 1
    if x < 0 and y < 0 and x > 7 and y > 7:
        return posy
    while True:
        if board[x][y+i] != color and board[x][y+i] != 0 and y+i <= 7:
            posy.append(y + i)
            i +=1
        else:
            break
    a = [x, posy]
    return a

def replace_rightleft(board,x,y,color):
    posy = []
    i = 1
    if x < 0 and y < 0 and x > 7 and y > 7:
        return posy
    while True:
        if board[x][y-i] != color and board[x][y-i] != 0 and y-i >= 0:
            posy.append(y - i)
            i +=1
        else:
            break
    a = [x, posy]
    return a

def replace_diag_topleft_to_botright(board,x,y,color):
    posy = []
    posx = []
    i = 1
    if x < 0 and y < 0 and x > 7 and y > 7:
        return posy
    while True:
        if board[x+i][y+i] != color and board[x+i][y+i] !=0 and x+i <= 7 and y+i <= 7:
            posx.append(x + i)
            posy.append(y + i)
            i +=1
        else:
            break
    a = [posx, posy]
    return a

def replace_diag_botright_to_topleft(board,x,y,color):
    posy = []
    posx = []
    i = 1
    if x < 0 and y < 0 and x > 7 and y > 7:
        return posy
    while True:
        if board[x-i][y-i] != color and board[x-i][y-i] !=0 and x-i >= 0 and y-i >= 0:
            posx.append(x - i)
            posy.append(y - i)
            i +=1
        else:
            break
    a = [posx, posy]
    return a

def replace_diag_topright_to_botleft(board,x,y,color):
    posy = []
    posx = []
    i = 1
    if x < 0 and y < 0 and x > 7 and y > 7:
        return posy
    while True:
        if board[x+i][y-i] != color and board[x+i][y-i] !=0 and x+i <= 7 and y-i >= 0:
            posx.append(x + i)
            posy.append(y - i)
            i +=1
        else:
            break
    a = [posx, posy]
    return a

def replace_diag_botleft_to_topright(board,x,y,color):
    posy = []
    posx = []
    i = 1
    if x < 0 and y < 0 and x > 7 and y > 7:
        return posy
    while True:
        if board[x-i][y+i] != color and board[x-i][y+i] !=0 and x-i >= 0 and y+i <= 7:
            posx.append(x - i)
            posy.append(y + i)
            i +=1
        else:
            break
    a = [posx, posy]
    return a

def reverce_count(board,x,y,color):
    i = 0
    if board[x][y] != 0:
        return i
    a1 = replace_topdown(board, x, y, color)
    a2 = replace_bottomup(board, x, y, color)
    a3 = replace_leftright(board, x, y, color)
    a4 = replace_rightleft(board, x, y, color)
    a5 = replace_diag_botleft_to_topright(board, x, y, color)
    a6 = replace_diag_botright_to_topleft(board, x, y, color)
    a7 = replace_diag_topleft_to_botright(board, x, y, color)
    a8 = replace_diag_topright_to_botleft(board, x, y, color)
    if a1[0] != []:
        for z in range(len(a1[0])):
            i += 1
    if a2[0] != []:
        for z in range(len(a2[0])):
            i += 1
    if a3[1] !=[]:
        for z in range(len(a3[1])):
            i += 1
    if a4[1] != []:
        for z in range(len(a4[1])):
            i += 1
    if a5[0] != []:
        for z in range(len(a5[0])):
            i += 1
    if a6[0] != []:
        for z in range(len(a6[0])):
            i += 1
    if a7[0] != []:
        for z in range(len(a7[0])):
            i += 1
    if a8[0] != []:
        for z in range(len(a8[0])):
            i += 1
    return i

def compute_counts(board, color):
    board_count = create_board()
    for i in range(7):
        for j in range(7):
            if j+1 <= 8 and j-1 >= 0 and i+1 <= 8 and i-1 >= 0:
                if board[i][j] == 0 and board[i][j+1] != 0 or board[i][j-1] != 0 or board[i+1][j] != 0 or board[i-1][j] != 0:
                    if board[i][j+1] != color or board[i][j-1] != color or board[i+1][j] != color or board[i-1][j] != color:
                        board_count[i][j] = reverce_count(board, i, j, color)
    return board_count

def add_checker(board, x, y, color):
    board[x][y] = color
    a1 = replace_topdown(board, x, y, color)
    a2 = replace_bottomup(board, x, y, color)
    for z in range(len(a1[0])):
        board[a1[0][z]][y] = color
    for z in range(len(a2[0])):
        board[a2[0][z]][y] = color
    a3 = replace_leftright(board, x, y, color)
    a4 = replace_rightleft(board, x, y, color)
    for z in range(len(a3[1])):
        board[x][a3[1][z]] = color
    for z in range(len(a4[1])):
        board[x][a4[1][z]] = color
    a5 = replace_diag_botleft_to_topright(board, x, y, color)
    a6 = replace_diag_botright_to_topleft(board, x, y, color)
    for z in range(len(a5[0])):
        board[a5[0][z]][a5[1][z]] = color
    for z in range(len(a6[0])):
        board[a6[0][z]][a6[1][z]] = color
    a7 = replace_diag_topleft_to_botright(board, x, y, color)
    a8 = replace_diag_topright_to_botleft(board, x, y, color)
    for z in range(len(a7[0])):
        board[a7[0][z]][a7[1][z]] = color
    for z in range(len(a8[0])):
        board[a8[0][z]][a8[1][z]] = color
    return board

def human_play(board, color):
    move = False
    while True:
        x = int(input("Give the row:"))
        y = int(input("Give column:"))
        if x < 0 and y < 0 and x > 7 and y > 7:
            break
        else:
            a = reverce_count(board, x, y, color)
            if a != 0:
                move = True
                add_checker(board, x, y, color)
                break
    return move

def computer_play(board):
    color = 2
    a = compute_counts(board, color)
    b = 0
    for i in range(8):
        for j in range(8):
            if a[i][j] > b:
                b = a[i][j]
                ai = i
                aj = j
    if b == 0:
        move = False
    else:
        add_checker(board, ai, aj, color)
        move = True
    return move


def print_score(board):
    p1 = 0
    p2 = 0
    for z in range(8):
        for t in range(8):
            if board[z][t] == 1:
                p1 +=1
            elif board[z][t] == 2:
                p2 +=2
            else:
                pass
    print("Player1 Score:", p1)
    print("Player2 Score:", p2)
    return p1, p2



pn = int(input("Give the number of palyers:"))
board = create_board()
if pn ==1:
    playercolor = 1
    i = 0
    while True:
        print_board(board)
        pl = human_play(board,playercolor)
        com = computer_play(board)
        print_board(board)
        score = print_score(board)
        if pl == False and com == False:
            break
        i += 1
        if i == 60:
            break
    score = list(score)
    if score[1] > score[2]:
        print("YOU WIN!!!")
    elif score[1] < score[2]:
        print("YOU LOSE!!!")
    else:
        print("DRAW")
elif pn == 2:
    player1color = 1
    player2color = 2
    i = 0
    while True:
        print_board(board)
        pl1 = human_play(board, player1color)
        print_board(board)
        pl2 = human_play(board, player2color)
        print_board(board)
        score = print_score(board)
        if pl1 == False and pl2 == False:
            break
        i +=1
        if i == 60:
            break
    score = list(score)
    if score[1] > score[2]:
        print("PLAYER1 WINS!!!")
    elif score[1] < score[2]:
        print("PLAYER2 WINS!!!")
    else:
        print("DRAW")
