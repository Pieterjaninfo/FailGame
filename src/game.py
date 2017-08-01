import pygame
import random
pygame.init()

# Initialize variables
version = 1.0
display_width = 800
display_heigth = 600
resources_path = '../resources/'

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
purple = (148,0,211)
yellow = (255,255,0)

car_width = 56
car_height = 80
car_speed = 5
base_shoot_cd = 30

pause = False
sound_playing = False
difficulty_adjusted = False

gameDisplay = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption('NEW GTA TOTALLY NOT OVERHYPED KAPPA GAME nomansbuy 2.0')
clock = pygame.time.Clock()
carImg1 = pygame.image.load(resources_path + 'car.png')
carImg2 = pygame.image.load(resources_path + 'BestGameCarLmao.png')
carImg3 = pygame.image.load(resources_path + 'dildowcar.png')
carImg4 = pygame.image.load(resources_path + 'lambo.png')
icon = pygame.image.load(resources_path + 'bin.png')
img_bg2 = pygame.image.load(resources_path + 'sanicpepe.png')
rocket = pygame.image.load(resources_path + 'rocket.png')

selected_car = carImg1

crash_sound = pygame.mixer.Sound(resources_path + 'Lol U Died.wav')
pause_sound = pygame.mixer.Sound(resources_path + 'GetUrAssBackThere.wav')
intro_sound = pygame.mixer.Sound(resources_path + 'DialUp Internet.wav')
intro_sound2 = pygame.mixer.Sound(resources_path + 'Oh Hello There.wav')
ding_sound = pygame.mixer.Sound(resources_path + 'Ding.wav')
explosion_sound = pygame.mixer.Sound(resources_path + 'Explosion.wav')
explosion_sound2 = pygame.mixer.Sound(resources_path + 'Object Crash Sound.wav')
splat_sound = pygame.mixer.Sound(resources_path + 'Splat.wav')
play_music = pygame.mixer.music.load(resources_path + 'despacito.wav')

pygame.display.set_icon(icon)

def draw_score(pretext, count, location):
    font = pygame.font.SysFont(None, 24)
    text = font.render(pretext + str(count) + " nuts", True, black)
    gameDisplay.blit(text, location)


def things(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])


def car(x,y):
    gameDisplay.blit(selected_car, (x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def title_display(text, font, x, y):
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)


def text_display(text, font, location):
    TextSurf, TextRect = text_objects(text, font)
    TextRect = location
    gameDisplay.blit(TextSurf, TextRect)


def difficulty_settings(score):
    global play_music
    global car_speed
    global difficulty_adjusted

    if score < 10:
        gameDisplay.fill(white)
    elif score < 20:
        gameDisplay.fill(green)
    elif score < 30:
        gameDisplay.fill(blue)
    else:
        gameDisplay.fill(yellow)
        gameDisplay.blit(img_bg2, (0,0))

    if not difficulty_adjusted:
        if score == 10:
            car_speed += 3
            pygame.mixer.music.stop()
            play_music = pygame.mixer.music.load(resources_path + 'despacito2.wav')
            pygame.mixer.music.play(-1)
            difficulty_adjusted = True
        elif score == 20:
            car_speed += 3
            pygame.mixer.music.stop()
            play_music = pygame.mixer.music.load(resources_path + 'despacito3.wav')
            pygame.mixer.music.play(-1)
            difficulty_adjusted = True
        elif score == 30:
            car_speed += 3
            pygame.mixer.music.stop()
            play_music = pygame.mixer.music.load(resources_path + 'BITCHES AINT SHIT.wav')
            pygame.mixer.music.play(-1)
            difficulty_adjusted = True

    if score == 19 or score == 29:
        difficulty_adjusted = False


def crash():
    global play_music
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    play_music = pygame.mixer.music.load(resources_path + 'despacito.wav')

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


def car_button(car_img, x, y, cw, ch, cs):
    global selected_car, car_width, car_height, car_speed
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    w, h = 60, 80

    if x < mouse[0] < x+w and y < mouse[1] < y+h:
        if click[0] == 1:
            selected_car = car_img
            car_width = cw
            car_height = ch
            car_speed = cs

    if selected_car == car_img:
        pygame.draw.rect(gameDisplay, bright_green, (x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, blue, (x,y,w,h))

    gameDisplay.blit(pygame.transform.scale(car_img, (cw, 80)), (x+w/2-cw/2,y))


def unpause():
    global pause
    pause = False


def paused():
    pygame.mixer.music.stop()
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
    pygame.mixer.music.play(-1)


def game_intro():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(random.choice([intro_sound, intro_sound2]))
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.K_KP_ENTER or event.type == pygame.K_SPACE:
                intro = False
                game_loop()

        gameDisplay.fill(white)

        text_display('Version: ' + str(version), pygame.font.Font('freesansbold.ttf', 15), (0,0))

        title_display("ayy lmaooo sim2k17", pygame.font.Font('freesansbold.ttf', 80), display_width/2, display_heigth/3)

        car_button(carImg1, display_width/4, 300, 56, 80, 5)
        car_button(carImg2, display_width/4+100, 300, 56, 80, 10)
        car_button(carImg3, display_width/4+200, 300, 56, 80, 5)
        car_button(carImg4, display_width/4+300, 300, 10, 150, 1)


        button("GO~!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Fkoff", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause, car_speed
    pygame.mixer.music.play(-1)
    x = display_width * 0.5
    # y = display_heigth * 0.8
    y = display_heigth - car_height - 20
    x_change = 0

    thing_x = random.randrange(0, display_width)
    thing_y = -600
    thing_speed = 5
    thing_w = 100
    thing_h = 100

    shoot_cd = 0
    rocket_x = -1
    rocket_y = -1

    if selected_car == carImg1 or selected_car == carImg3:
        car_speed = 5
    elif selected_car == carImg2:
        car_speed = 10
    else:
        car_speed = 1

    dodged = 0
    destroyed = 0
    moves = list()
    gameExit = False
    while not gameExit:

        #input handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                    game_intro()

                if event.key == pygame.K_LEFT:
                    moves.insert(0, 'left')
                if event.key == pygame.K_RIGHT:
                    moves.insert(0, 'right')
                if event.key == pygame.K_p:
                    pause = True
                    paused()

                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    if selected_car == carImg3 and shoot_cd == 0:
                        rocket_x = x + car_width/2
                        rocket_y = y
                        shoot_cd = base_shoot_cd

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moves.pop(moves.index("left"))
                if event.key == pygame.K_RIGHT:
                    moves.pop(moves.index("right"))

            if len(moves) > 0:
                if moves[0] == "left":
                    x_change = -car_speed
                elif moves[0] == "right":
                    x_change = car_speed
            else:
                x_change = 0

        x += x_change
        thing_y += thing_speed
        rocket_y -= 20

        # set background
        difficulty_settings(dodged)

        things(thing_x, thing_y, thing_w, thing_h, black)
        car(x,y)
        gameDisplay.blit(rocket, (rocket_x, rocket_y))
        draw_score("Juked ", dodged, (0,0))
        if selected_car == carImg3:
            draw_score("Rekt ", destroyed, (0, 30))

        if x > display_width - car_width or x < 0:  #car hitting border
            crash()

        if thing_y < rocket_y < thing_y + thing_h and thing_x < rocket_x < thing_x + thing_w: #rocket hitting thing
            pygame.mixer.Sound.play(splat_sound)
            thing_x = -600 - thing_y
            thing_y = random.randrange(0, display_width)
            destroyed += 1
            dodged += 1


        if thing_y > display_heigth:    #object out of screen
            pygame.mixer.Sound.play(ding_sound)
            thing_y = 0 - thing_h
            thing_x = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1

        if y < thing_y + thing_h and y + car_height > thing_y: #collision
            if thing_x < x < thing_x + thing_w or thing_x < x+car_width < thing_x + thing_w:
                pygame.mixer.Sound.play(random.choice([explosion_sound, explosion_sound2]))
                crash()

        if shoot_cd > 0:
            shoot_cd -= 1

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    game_intro()
    quitgame()
