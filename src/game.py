import pygame
import time
import random
pygame.init()

# Initialize variables
display_width = 800
display_heigth = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)

car_width = 56
car_height = 70

pause = False

gameDisplay = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption('NEW GTA TOTALLY NOT OVERHYPED KAPPA GAME nomansbuy 2.0')
clock = pygame.time.Clock()
carImg = pygame.image.load('BestlGameCarLmao.png')
icon = pygame.image.load('garbagebin.png')

crash_sound = pygame.mixer.Sound('Lol U Died.wav')
pause_sound = pygame.mixer.Sound('GetUrAssBackThere.wav')
intro_sound = pygame.mixer.Sound('DialUp Internet.wav')
# play_music = pygame.mixer.music.load('music.wav')

pygame.display.set_icon(icon)

def things_dodged(count):
    font = pygame.font.SysFont(None, 24)
    text = font.render("~Juked: " + str(count) + " bois", True, black)
    gameDisplay.blit(text, (0,0))


def things(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])


def car(x,y):
    gameDisplay.blit(carImg, (x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def title_display(text, font, x, y):
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)


def text_display(text, font):
    TextSurf, TextRect = text_objects(text, font)
    TextRect = (display_width/2, display_heigth/2)
    gameDisplay.blit(TextSurf, TextRect)


def crash():
    # pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()

        title_display("You ded boi", pygame.font.Font('freesansbold.ttf', 100), display_width/2, display_heigth/2)

        button("Cum agen", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Rope self", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def quitgame():
    pygame.quit()
    quit()


def button(msg, x, y, w, h, c, c_hover, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x+w and y < mouse[1] < y+h:
        pygame.draw.rect(gameDisplay, c_hover, (x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, c, (x,y,w,h))

    title_display(msg, pygame.font.Font('freesansbold.ttf', 20), x+w/2, y+h/2)


def unpause():
    global pause
    pause = False


def paused():
    pygame.mixer.Sound.play(pause_sound)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    unpause()

        gameDisplay.fill(white)
        title_display("paused ay bruv", pygame.font.Font('freesansbold.ttf', 80), display_width/2, display_heigth/2)

        button("LEZ GO", 150, 450, 100, 50, green, bright_green, unpause)
        button("End lyf", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    pygame.mixer.Sound.play(intro_sound)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.K_SPACE:
                intro = False

        gameDisplay.fill(white)
        title_display("ayy lmaooo sim2k17", pygame.font.Font('freesansbold.ttf', 80), display_width/2, display_heigth/2)

        button("GO~!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Fkoff", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    # pygame.mixer.music.play(-1)
    x = display_width * 0.45
    y = display_heigth * 0.8
    x_change = 0

    thing_x = random.randrange(0, display_width)
    thing_y = -600
    thing_speed = 4
    thing_w = 100
    thing_h = 100

    dodged = 0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        thing_y += thing_speed

        gameDisplay.fill(white)
        things(thing_x, thing_y, thing_w, thing_h, black)
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_y > display_heigth:
            thing_y = 0 - thing_h
            thing_x = random.randrange(0, display_width)
            dodged += 1
            # thing_speed += 1
            thing_w += dodged * 1.2

        if y < thing_y + thing_h and y + car_height > thing_y:
            if thing_x < x < thing_x + thing_w or thing_x < x+car_width < thing_x + thing_w:
                crash()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_intro()
    game_loop()
    quitgame()
