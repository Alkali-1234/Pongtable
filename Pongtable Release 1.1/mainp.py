import pygame
from paddle import Paddle
from ball import Ball
from button import button
import datetime
pygame.init()
# paddle color
color = 255, 255, 255
# datetime
d = datetime.datetime.utcnow()
# screen setup
screen = pygame.display.set_mode([500, 800])
# title and icon
pygame.display.set_caption("Pong table")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)
# sprite 1
sprite_group = pygame.sprite.Group()
paddle = Paddle(color, 100, 10)
paddle.rect.x = (screen.get_width()/2) - (paddle.rect.width/2)
paddle.rect.y = 600
# sprite 2
ball = Ball((0, 0, 0), 10, 10)
ball.rect.x = 345
ball.rect.y = 195
# add sprites
sprite_group.add(paddle)
sprite_group.add(ball)
# log msg
log = f"Starting... \n"
# def's


def write_log():
    with open("log.txt", "a") as f:
        f.write(str(log))


def redraw_window():
    green_button.draw(screen)


word1 = "Welcome To Pong table"
word2 = "By: Alkali1234"
# clock
clock = pygame.time.Clock()
Time = 0
# scores
score = 0
# Game Running
R = 0
B = 0
# Game Over
game_over = "Game over"
# button


# set running
write_log()
running = True
green_button = button((255, 255, 255), 345, 195, 100, 50, 'Start')
while running:
    screen.fill((0, 255, 0))
    clock.tick(60)
    Time = (Time + 0.01)
    sprite_group.draw(screen)
    if B == 0:
        redraw_window()
    # Welcoming
    if Time <= 3:
        font3 = pygame.font.SysFont("Arial", 50)
        text3 = font3.render(str(word1), 1, (255, 255, 255))
        screen.blit(text3, (15, 250))
        font4 = pygame.font.SysFont("Arial", 50)
        text4 = font4.render(str(word2), 1, (255, 255, 255))
        screen.blit(text4, (15, 300))
    # collision
    if pygame.sprite.collide_mask(ball, paddle):
        ball.bounce()
        score += 1
    # display score
    font = pygame.font.SysFont("Arial", 60)
    text = font.render(str(score), 1, (255, 255, 255))
    screen.blit(text, (20, 20))
    # events
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if green_button.isOver(pos):
                R = 1
                B = 1
        if event.type == pygame.MOUSEMOTION:
            if green_button.isOver(pos):
                green_button.color = 0, 0, 255
            else:
                green_button.color = 255, 255, 255
    pygame.display.update()
    if R == 1:
        sprite_group.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left(10)
            log = f"Time: {d} Act: Key left pressed \n"
            write_log()
        if keys[pygame.K_RIGHT]:
            paddle.move_right(10, 400)
            log = f"Time: {d} Act: Key Right pressed \n"
            write_log()
        if ball.rect.x >= screen.get_width():
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 2:

            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y <= 2:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y >= screen.get_height():
            ball.stop()
            font2 = pygame.font.SysFont("Arial", 60)
            text2 = font2.render(str(game_over), 1, (255, 255, 255))
            screen.blit(text2, (250, 250))
            running = False
        # display info printing and update system
        print(f"Fps: {clock}")
        print(f"Time: {Time}")

# finals
log = f"Time: {d} Act: Stopping... \n"
write_log()
print(f"Score: {score}")
ball.stop()
pygame.quit()
