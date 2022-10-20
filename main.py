import piece

board = []
for i in range(8):
    board.append([None,None,None,None,None,None,None,None]) 

boardSetUp = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
for i in range(8): 
    board[0][i] = piece.Piece(i, 0, "black", boardSetUp[i])
    board[1][i] = piece.Piece(i, 0, "black", "pawn")
    board[7][i] = piece.Piece(i, 0, "white", boardSetUp[i])
    board[6][i] = piece.Piece(i, 0, "white", "pawn")

print(board)