import pygame
import os 
from model import RedHood

window = (1000, 700)

canvas = pygame.display.set_mode(window)

background = (50, 50, 50)
last_time = pygame.time.get_ticks()
animation_cooldown = 50
frame = 0

move_left = False
move_right = False

redhood_size = 3
cooldown_attack = 500

# redhood_move_frames = len([name for name in os.listdir('./character/redhood/move') if os.path.isfile(name)])

image_sprite = list()
# redhood move 
# for i in range(0, 25):
    # redhood_image = pygame.image.load("./character/redhood/move/redhood_{}.png".format(i))
    # redhood_image_turn_arround = pygame.image.load("./character/redhood/move/run_turn_arround_{}.png".format(i))
    # redhood_image_flip = pygame.transform.flip(redhood_image, True, False)
    # redhood_image_scale = pygame.transform.scale(redhood_image, redhood_size)
    # image_sprite.append(redhood_image_scale)

# redhood turn arround
# for i in range(0, 5):
    # redhood_image_turn_arround = pygame.image.load("./character/redhood/turn_arround/run_turn_arround_{}.png".format(i))
redhood = RedHood(dx=200, dy=200, scale=redhood_size)
clock = pygame.time.Clock()
run = True
# pygame.display.flip()
while run:
    move = True
    canvas.fill(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
                redhood.update_action(action='idle')
            if event.key == pygame.K_d:
                move_right = False
                redhood.update_action(action='idle')
            if event.key == pygame.K_SPACE:
                # redhood.finish_action = False
                redhood.update_action(action='idle')

        if event.type == pygame.MOUSEBUTTONUP:
            redhood.update_action(action='idle')
    
    key_input = pygame.key.get_pressed()
    if key_input:
        if key_input[pygame.K_d] and key_input[pygame.K_SPACE]:
            move_right = True       
            redhood.update_action(action='jump')
        if key_input[pygame.K_a]:
            move_left = True        
            redhood.update_action(action='move')
        if key_input[pygame.K_d]:
            move_right = True
            redhood.update_action(action='move')
        if key_input[pygame.K_SPACE]:
            redhood.update_action(action='jump')
            # redhood.jumping = True
            
    left_mouse, middle_mouse, right_mouse = pygame.mouse.get_pressed()
    if left_mouse:
        if pygame.time.get_ticks() - redhood.time  < cooldown_attack:
            redhood.click += 1
            if redhood.click > 3:
                redhood.click = 1
            redhood.update_action(action='attack')


    redhood.update_animation()
    redhood.move(move_left=move_left, move_right=move_right)
    redhood.draw(canvas=canvas)
    
    # canvas.blit(image_sprite[frame], (200, 200))
    # clock.tick(45)dddddddddddddddddddddddddddddd
    pygame.display.update()
    
   