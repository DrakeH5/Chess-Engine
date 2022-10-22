def RookMoves(x, y, color, board):
    possibleMoves=[] 
    
    
    for i in range(7): 
        if y+i < 8: 
            if board[y+i][x] == None: 
                possibleMoves.append([x, y+i])
            elif board[y+i][x].color != color: 
                possibleMoves.append([x, y+i])
            else: 
                i = 8
    for i in range(7): 
        if y-i > -1: 
            if board[y-i][x] == None: 
                possibleMoves.append([x, y-i])
            elif board[y-i][x].color != color: 
                possibleMoves.append([x, y-i])
            else: 
                i = 8
    for i in range(7): 
        if x+i < 8: 
            if board[y][x+i] == None: 
                possibleMoves.append([x+i, y])
            elif board[y][x+i].color != color: 
                possibleMoves.append([x+i, y])
            else: 
                i = 8
    for i in range(7): 
        if x-i > -1: 
            if board[y][x-i] == None: 
                possibleMoves.append([x-i, y])
            elif board[y][x-i].color != color: 
                possibleMoves.append([x-i, y])
            else: 
                i = 8


    return possibleMoves #return all possible moves