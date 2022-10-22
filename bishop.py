def BishopMoves(x, y, color, board):
    possibleMoves=[] 
    
    for i in range(7): 
        if y+i < 8 and x+i < 8: 
            if board[y+i][x+i] == None: 
                possibleMoves.append([x+i, y+i])
            elif board[y+i][x+i].color != color: 
                possibleMoves.append([x+i, y+i])
            else: 
                i = 8
    for i in range(7): 
        if y-i > -1 and x+i < 8: 
            if board[y-i][x+i] == None: 
                possibleMoves.append([x+i, y-i])
            elif board[y-i][x+i].color != color: 
                possibleMoves.append([x+i, y-i])
            else: 
                i = 8
    for i in range(7): 
        if y+i < 8 and x-i > -1: 
            if board[y+i][x-i] == None: 
                possibleMoves.append([x-i, y+i])
            elif board[y+i][x-i].color != color: 
                possibleMoves.append([x-i, y+i])
            else: 
                i = 8
    for i in range(7):
        if y-i > -1 and x-i > -1:  
            if board[y-i][x-i] == None: 
                possibleMoves.append([x-i, y-i])
            elif board[y-i][x-i].color != color: 
                possibleMoves.append([x-i, y-i])
            else: 
                i = 8


    return possibleMoves #return all possible moves