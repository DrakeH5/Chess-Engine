import piece

board = []
for i in range(9):
    board.append(["","","","","","","",""]) 

pawn1 = piece.Piece(1, 1, "white", "pawn")
print(pawn1.color)
print(board)