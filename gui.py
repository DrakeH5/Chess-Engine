from select import select
from turtle import clone
import main

import pawn
pawnMoves = pawn.PawnMoves

import bishop
bishopMoves = bishop.BishopMoves

import rook
rookMoves = rook.RookMoves

import knight
knightMoves = knight.KnightMoves

import queen
queenMoves = queen.QueenMoves

import king
kingMoves = king.KingMoves

import allPossibleMoves
findAllMoves = allPossibleMoves.findAllMoves

import math

import copy

import sys, pygame
pygame.init()

pygame.font.init()

size = width, height = 500, 500
white = 200, 200, 200
black = 0, 0, 0

screen = pygame.display.set_mode(size)


def DrawBoardAndPieces():
    screen.fill(white)
    #background
    screen.fill(black)
    #outline
    rect = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(screen, white, rect, 1)

    #tiles
    for i in range(8):
        for j in range(8):  
            rect = pygame.Rect(j*(width/8), i*(height/8), width/8, height/8)
            pygame.draw.rect(screen, white, rect, (j+i)%2)

    #draw name of pieces
    font = pygame.font.SysFont('freesanbold.ttf', 30)
    for i in range(8):
        for j in range(8): 
            if main.board[i][j] != None: 
                if main.board[i][j].color == white: 
                    text = font.render(main.board[i][j].type, True, main.board[i][j].color, black)
                else: 
                    text = font.render(main.board[i][j].type, True, main.board[i][j].color, white)
                textRect = text.get_rect()
                textRect.center = (j*(width/8)+(width/16) , i*(height/8)+(height/16))
                screen.blit(text, textRect)

DrawBoardAndPieces()

selected = None
possibleMoves = None

teams=["white", "black"]
turn=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #end 

        #click on screen
        if event.type == pygame.MOUSEBUTTONUP: 
            pos = pygame.mouse.get_pos()
            pos = math.floor(pos[0]/(width/8)), math.floor(pos[1]/(height/8))
            if selected != None and possibleMoves != None: 
                if [pos[0], pos[1]] in possibleMoves:
                    main.board[selected.y][selected.x] = None
                    OldSelected = copy.copy(selected)
                    selected.x = pos[0]
                    selected.y = pos[1]
                    OldSpace = copy.copy(main.board[pos[1]][pos[0]])
                    main.board[pos[1]][pos[0]] = selected
                    for i in range(8): 
                        for j in range(8):
                            if main.board[i][j] != None and main.board[i][j].type == "king" and main.board[i][j].color == teams[turn]: 
                                king = [main.board[i][j].x, main.board[i][j].y]
                    if king in findAllMoves(main.board, teams[abs(turn-1)]):
                        selected.x = OldSelected.x
                        selected.y = OldSelected.y
                        main.board[OldSelected.y][OldSelected.x] = selected
                        main.board[pos[1]][pos[0]] = OldSpace
                        turn = abs(turn-1)
                    turn = abs(turn-1)
                    DrawBoardAndPieces()
                selected = None
                possibleMoves = None    
            else: 
                selected = main.board[pos[1]][pos[0]]
                if selected != None and selected.color == teams[turn]:
                    getMoves = eval(selected.type + "Moves")
                    possibleMoves = getMoves(selected.x, selected.y, selected.color, main.board)


    pygame.display.flip()