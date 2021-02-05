import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("The Best Games")
screen = pygame.display.set_mode((500,500),0,32)


font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


    
def main_menu():
    while True:
        
        screen.fill((0,0,0))
        draw_text('Main Menu', font, (255,255,255), screen, 20, 20)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   pygame.quit()
                   sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(170, 140, 200, 50)
        button_2 = pygame.Rect(170, 250, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        
        draw_text('Games', font, (255,255,255), screen, 245, 160)
        draw_text('Options', font, (255,255,255), screen, 245, 270)

        
                    
        pygame.display.update()
        mainClock.tick(60)
        
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False
        
        draw_text('Games', font, (255,255,255), screen, 20, 20)
        draw_text('Press ESC to return', font, (255,255,255), screen, 350, 20)

        button_3 = pygame.Rect(170, 140, 200, 50)
        if button_3.collidepoint((mx, my)):
            if click:
                Table_Tennis()
                
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Table Tennis', font, (255,255,255), screen, 230, 160)

        
        pygame.display.update()
        mainClock.tick(60)
        
def options():
    running = True
    while running:
        screen.fill((0,0,0))
 
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC to return', font, (255,255,255), screen, 350, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
        
def Table_Tennis():
    running = True
    while running:
        screen.fill((0,0,0))
        draw_text('Press ESC to return', font, (255,255,255), screen, 350, 20)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

                   
main_menu()
