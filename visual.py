from select import select
import main

import pawn
pawnMoves = pawn.PawnMoves

import math

import sys, pygame
pygame.init()

pygame.font.init()

size = width, height = 500, 500
white = 200, 200, 200
black = 0, 0, 0

screen = pygame.display.set_mode(size)

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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() #end 

        #click on screen
        if event.type == pygame.MOUSEBUTTONUP: 
            pos = pygame.mouse.get_pos()
            pos = math.floor(pos[0]/(width/8)), math.floor(pos[1]/(height/8))
            selected = main.board[pos[1]][pos[0]]
            if selected != None:
                getMoves = eval(selected.type + "Moves")
                print(getMoves(pos[0], pos[1], selected.color, main.board))


    pygame.display.flip()
