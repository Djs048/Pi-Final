import pygame, sys
import random
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

        button_4 = pygame.Rect(170, 190, 200, 50)
        if button_4.collidepoint((mx, my)):
            if click:
                Snake()
                
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Table Tennis', font, (255,255,255), screen, 230, 160)

        pygame.draw.rect(screen, (255, 0, 0), button_4)
        draw_text('Snake', font, (255, 255, 255), screen, 230, 160)

        
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


def Snake():
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    snake_block = 10
    snake_speed = 15

    dis_width = 600
    dis_height = 400
 
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
    
    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, yellow)
        screen.blit(value, [0, 0])
 
 
 
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])
 
 
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
    def gameLoop():
        game_over = False
        game_close = False
 
        x1 = dis_width / 2
        y1 = dis_height / 2
 
        x1_change = 0
        y1_change = 0
 
        snake_List = []
        Length_of_snake = 1
 
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
        while not game_over:
 
            while game_close == True:
                screen.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()
 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
 
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            screen.fill(blue)
            pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
 
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
 
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
 
            pygame.display.update()
 
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
 
            mainClock.tick(snake_speed)
 
        pygame.quit()
        quit()
 
 
    gameLoop()


     
def Table_Tennis():
    running = True
    paddle1_y = 280
    paddle2_y = 280
    Start = False
    round_end = False
    ball_x = 250
    ball_y = 250
    ball_x_change = random.randrange(-3,3)
    ball_y_change = random.randrange(-3,3)
    Player1_score = 0
    Player2_score = 0
    
    
    while running:
        screen.fill((0,0,0))
        draw_text('Press ESC to return. Press SPACEBAR to start', font, (255,255,255), screen, 200, 20)
        draw_text('Player 1 use WASD to move. Player 2 use Arrow Keys to move.', font, (255,255,255), screen, 50, 60)
        keys = pygame.key.get_pressed()
        P1Score = "Score: {}".format(Player1_score)
        P2Score = "Score: {}".format(Player2_score)
        mx, my = pygame.mouse.get_pos()
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Start = True
                    round_end = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if keys[pygame.K_UP]:
            if (paddle2_y > 130):
                    paddle2_y += -5
        if keys[pygame.K_DOWN]:
            if (paddle2_y < 465):
                    paddle2_y += 5
        if keys[pygame.K_w]:
            if (paddle1_y > 130):
                    paddle1_y += -5
        if keys[pygame.K_s]:
            if (paddle1_y < 465):
                    paddle1_y += 5

        if round_end:
            play_again_button = pygame.Rect(195, 280, 100, 40)
            
            
            if (Player1_score == 3):
                Start = False
                draw_text("Player 1 Wins!", font, (255,255,255), screen, 200, 250)
                if play_again_button.collidepoint((mx, my)):
                    if click:
                        Player1_score = 0
                        Player2_score = 0
                        paddle1_y = 280
                        paddle2_y = 280
                        round_end = False
                        Start = True
                pygame.draw.rect(screen, (255, 0, 0), play_again_button)
                draw_text("Play Again", font, (255,255,255), screen, 210, 290)
                
            elif (Player2_score == 3):
                Start = False
                draw_text("Player 2 Wins!", font, (255,255,255), screen, 200, 250)
                if play_again_button.collidepoint((mx, my)):
                    if click:
                        Player1_score = 0
                        Player2_score = 0
                        paddle1_y = 280
                        paddle2_y = 280
                        round_end = False
                        Start = True
                pygame.draw.rect(screen, (255, 0, 0), play_again_button)
                draw_text("Play Again", font, (255,255,255), screen, 210, 290)
                
                
                
        
        if Start:
            if (ball_x_change == 0):
                ball_x_change = random.randrange(-3,3)
            if (ball_y_change == 0):
                ball_y_change = random.randrange(-3,3)

            if (ball_x < 60 and ball_x > 50) and (ball_y < paddle1_y + 40 and ball_y > paddle1_y): 
                ball_x_change *= -1
                        
            if (ball_x > 450 and ball_x < 460) and (ball_y < paddle2_y + 40 and ball_y > paddle2_y):
                ball_x_change *= -1
                
                
            if (ball_y < 125 or ball_y > 496):
                ball_y_change *= -1
                
            ball_x += ball_x_change
            ball_y += ball_y_change

            
            
            
            paddle_1 = pygame.Rect(50, paddle1_y, 10, 40)
            paddle_2 = pygame.Rect(450, paddle2_y, 10, 40)
            Top_Border = pygame.Rect(1, 125, 500, 5)
            Bottom_Border = pygame.Rect(1, 496, 500, 5)
        
            pygame.draw.rect(screen, (255, 0, 0), paddle_1)
            pygame.draw.rect(screen, (255, 0, 0), paddle_2)
            pygame.draw.rect(screen, (255, 0, 0), Top_Border)
            pygame.draw.rect(screen, (255, 0, 0), Bottom_Border)
            
            draw_text(P1Score, font, (255,255,255), screen, 30, 100)
            draw_text(P2Score, font, (255,255,255), screen, 430, 100)
            

            pygame.draw.circle(screen, (255, 255, 255), [ball_x, ball_y], 7)

            if (ball_x <= 0):
                ball_x = 250
                ball_y = 250
                Player2_score += 1
                ball_x_change = random.randrange(-3,3)
                ball_y_change = random.randrange(-3,3)
                round_end = True
                
                
            if (ball_x >= 500):
                ball_x = 250
                ball_y = 250
                Player1_score += 1
                ball_x_change = random.randrange(-3,3)
                ball_y_change = random.randrange(-3,3)
                round_end = True
                
                
        
       
        pygame.display.update()
        mainClock.tick(60)

                   
main_menu()
