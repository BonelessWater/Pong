import pygame
import math
import os
import neat

pygame.init()

# Initiating Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

rect_height = 50
rect_width = 200
ball_r = 50

ball_vx = 1
ball_vy = 7
acceleration = 2

paddle_movement = 6

score_counter = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

ping = pygame.Rect((SCREEN_WIDTH/2 - 100, 50, rect_width, rect_height))
pong = pygame.Rect((SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT - 100, rect_width, rect_height))
ball = pygame.Rect((SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 100, ball_r, ball_r))

def main(SCREEN_WIDTH, SCREEN_HEIGHT, ping, pong, ball, paddle_movement, acceleration, ball_vx, ball_vy, ball_r, score_counter):
    FPS = 60
    
    run = True
    while run:

        clock.tick(FPS)
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255), ball)
        pygame.draw.rect(screen, (255, 255, 255), ping)
        pygame.draw.rect(screen, (255, 255, 255), pong)

        if ball.x > SCREEN_WIDTH - ball_r:
            ball_vx = -ball_vx
        if ball.x < 0:
            ball_vx = -ball_vx

        # If the ball comes in contact with the paddle:
        if ball.y > pong.y - ball_r and ball.x + ball_r > pong.x and ball.x < pong.x + rect_width:
            v_mag = math.sqrt((ball_vx * ball_vx) + (ball_vy * ball_vy)) + acceleration

            # Gets angle depending on angle that the Ball hits paddle from its center
            theta = (5 / 4) * math.pi + ( (math.pi / 2) / rect_width) * (ball.x - pong.x)

            ball_vx = v_mag * math.cos(theta)
            ball_vy = v_mag * math.sin(theta)
            ball.move_ip(ball_vx, ball_vy)

        # If the ball comes in contact with the paddle:
        if ball.y < ping.y + rect_height and ball.x + ball_r > ping.x and ball.x < ping.x + rect_width:
            v_mag = math.sqrt((ball_vx * ball_vx) + (ball_vy * ball_vy)) + acceleration
            # Gets angle depending on angle that the Ball hits paddle from its center
            theta = (3 / 4) * math.pi - ( (math.pi / 2) / rect_width) * (ball.x - ping.x)

            ball_vx = v_mag * math.cos(theta)
            ball_vy = v_mag * math.sin(theta)
            ball.move_ip(ball_vx, ball_vy)
    
        # If ball Hits top or bottom
        if ball.y < 0:
            ball_vy = -ball_vy 
            score_counter += 1
            print(score_counter)
        if ball.y > SCREEN_HEIGHT - rect_height:
            ball_vy = -ball_vy

        ball.move_ip(ball_vx, ball_vy)
    
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True and ping.x > 0:
            ping.move_ip(-paddle_movement, 0)
        if key[pygame.K_d] == True and ping.x < SCREEN_WIDTH - rect_width:
            ping.move_ip(paddle_movement, 0)

        if key[pygame.K_j] == True and pong.x > 0:
            pong.move_ip(-paddle_movement, 0)
        if key[pygame.K_l] == True and pong.x < SCREEN_WIDTH - rect_width:
            pong.move_ip(paddle_movement, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

main(SCREEN_WIDTH, SCREEN_HEIGHT, ping, pong, ball, paddle_movement, acceleration, ball_vx, ball_vy, ball_r, score_counter)
