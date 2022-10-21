def PawnMoves(x, y, color, board):
    if color=="white": 
        direction=-1
    elif color=="black": 
        direction=1
    possibleMoves=[]
    if color=="black" and y==1 or color=="white" and y==6: 
        if board[y+(direction*2)][x] == None:
            possibleMoves.append([y+(direction*2), x])
    if  board[y+direction][x+1] != None and board[y+direction][x+1].color != color:  
        possibleMoves.append([y+direction, x+1])
    if board[y+direction][x-1] != None and board[y+direction][x-1].color != color:  
        possibleMoves.append([y+direction, x-1])
    if board[y+direction][x] == None: 
        possibleMoves.append([y+direction, x])
    return possibleMoves