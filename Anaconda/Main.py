import pygame
import sys
import os
import time
import random
from DrawOnScreen import *
from Snake import *
from Objectives import *

sys.path.append('C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/Anaconda/')
path = 'C:/Users/marios/Documents/Tutorials-Projects/Personal/Python-VScode/ThesisRetroArcadeGamingMachine/Anaconda/Sound_Images/'

#Graphics
os.environ['SDL_VIDEO_CENTERED'] = '1'

def game_Start():
    pygame.init()

    #Adapt Window Graphics
    info = pygame.display.Info()
    display_width = info.current_w
    display_height = info.current_h
    #display_width = 700
    #display_height = 700

    gameDisplay = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
    pygame.display.set_caption("Snake")

    FPS = 8
    clock = pygame.time.Clock()
    image_size = 30

    def check_Input(screen):
        screen.show_Screen()
        pygame.display.flip()
        waiting = True
        k = 1
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    else:
                        waiting = False
                        return k


    screen = DrawWindows(gameDisplay, display_width, display_height)
    screen.set_Image(1)
    check_Input(screen)
    screen.set_Image(2)
    speedx_right = image_size
    speedx_left = -image_size
    speedy_up = -image_size
    speedy_down = image_size

    def game_loop():
        #sound
        high_as_fuck_sound = path + 'royalty-free-arcade-game-background-music-breeze.wav'
        play_music = 1

        #Objectives and player sprite lists
        all_sprites_list = pygame.sprite.Group()
        all_sprites_list.add(screen)

        snake_positions_list = []
        #snake = Snake(display_width, display_height,screen.WHITE)
        snake_head_list = pygame.sprite.Group()
        snake_head = snake_Head(display_width, display_height, screen.WHITE)
        snake_head_list.add(snake_head)
        all_sprites_list.add(snake_head)

        snake_body_list = []#pygame.sprite.Group()
        snake_body = snake_Body(display_width, display_height, screen.WHITE, 1)
        snake_body_list.append(snake_body)
        #snake_body_list.add(snake_body)
        all_sprites_list.add(snake_body)

        fruit = Objectives(display_width, display_height)
        fruit.set_Image(1, screen.WHITE)
        objective_list = pygame.sprite.Group()
        objective_list.add(fruit)
        all_sprites_list.add(fruit)
        init_list = 1
        #snake.set_Body_List()
        game_score = 0
        snake_length = 2
        new_bodyx = 0
        new_bodyy = 0

        if init_list == 1:
            for snake_head in snake_head_list:
                snake_head.set_Init_Position()
                snake_positions_list.append(snake_head.x)
                snake_positions_list.append(snake_head.y)
            for snake_body in snake_body_list:
                snake_body.speedx = 30
                snake_body.speedy = 0
                snake_body.set_Init_Position()
                snake_positions_list.append(snake_body.x)
                snake_positions_list.append(snake_body.y)
            init_list = 0

        game_Over = False
        move_head = 0
        i = 0
        while not game_Over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True      
                elif event.type == pygame.KEYDOWN:
                    for snake_head in snake_head_list:
                        if event.key == pygame.K_LEFT:
                            if snake_head.rotation != 1:
                                snake_head.set_Direction(speedx_left, 0, 2)
                        elif event.key == pygame.K_RIGHT:
                            if snake_head.rotation != 2:
                                snake_head.set_Direction(speedx_right , 0, 1)
                        elif event.key == pygame.K_UP:
                            if snake_head.rotation != 4:
                                snake_head.set_Direction(0, speedy_up, 3)
                        elif event.key == pygame.K_DOWN:
                            if snake_head.rotation != 3:
                                snake_head.set_Direction(0, speedy_down, 4) 
                        move_head = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        game_Over = True
                        pygame.quit()
                        return
            move_head = 1

            #Move all bodies
            for i in range(len(snake_body_list) - 1, 0, -1):
                x = snake_body_list[i - 1].x
                y = snake_body_list[i - 1].y
                snake_body_list[i].x = x
                snake_body_list[i].y = y
                snake_body_list[i].set_Image()
                
            #Move second body
            if len(snake_body_list) > 0:
                x = snake_head.x
                y = snake_head.y
                snake_body_list[0].x = x
                snake_body_list[0].y = y
                snake_body_list[0].set_Image()

            if move_head == 1 and snake_head.alive == 1:
                snake_head.move()

            k = 0
            body_length = 0
            body_length = (len(snake_body_list)) - 1

            if len(snake_body_list) == 2:
                i = 0
                while i < len(snake_body_list):
                    print("Snake body "+str(i)+" x: "+str(snake_body_list[i].x))
                    print("Snake body "+str(i)+" y: "+str(snake_body_list[i].y))
                    i += 1

            for i in range(0, body_length , 1):
                #if (snake_head.x >= snake_body_list[i].rect.left) and (snake_head.x <= snake_body_list[i].rect.right) and (snake_head.y >= snake_body_list[i].rect.top) and (snake_head.y <= snake_body_list[i].rect.bottom):
                if (snake_head.x == snake_body_list[i].rect.x) and (snake_head.y == snake_body_list[i].rect.y):
                    snake_head.alive = 0

            #check snake - fruit collision
            add_score = 0
            add_score = fruit_collision(snake_head_list, objective_list, all_sprites_list)
            game_score = game_score + add_score
            if add_score == 1:
                snake_length += 1
                snake_body = snake_Body(display_width, display_height, screen.WHITE, 2)
                snake_body_list.append(snake_body)
                snake_body.set_Image()
                all_sprites_list.add(snake_body) 
                add_score = 0

            #play background music
            for snake_head in snake_head_list:
                if snake_head.alive == 1 and play_music == 1:
                    pygame.mixer.music.load(high_as_fuck_sound)
                    pygame.mixer.music.play(-1)
                    play_music += 1
                elif snake_head.alive == 0:
                    game_Over = True
                    pygame.mixer.music.stop()
                    screen.game_Over('YOU LOST! FINAL SCORE: ' + str(game_score), 40)

            snake_positions_list[0] = snake_head.rect.x
            snake_positions_list[1] = snake_head.rect.y
            
            #gameDisplay.fill(screen.GREEN)
            #screen.show_Background()
            all_sprites_list.draw(gameDisplay)
            all_sprites_list.update()
            screen.draw_Text('Score:' + str(game_score), 40, display_width / 2, 10)
            pygame.display.update()
            clock.tick(FPS)

    game_loop()
    pygame.quit()
    return