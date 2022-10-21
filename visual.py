import main

import sys, pygame
pygame.init()

pygame.font.init()

size = width, height = 500, 500
white = 200, 200, 200
black = 0, 0, 0

screen = pygame.display.set_mode(size)

screen.fill(black)

rect = pygame.Rect(0, 0, width, height)
pygame.draw.rect(screen, white, rect, 1)

for i in range(8):
    for j in range(8):  
        rect = pygame.Rect(j*(width/8), i*(height/8), width/8, height/8)
        pygame.draw.rect(screen, white, rect, (j+i)%2)


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
        if event.type == pygame.QUIT: sys.exit()


    pygame.display.flip()
