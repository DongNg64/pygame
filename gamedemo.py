import pygame
import os 
from model import RedHood

window = (1000, 700)
clock = pygame.time.Clock()
canvas = pygame.display.set_mode(window)

background = (50, 50, 50)
last_time = pygame.time.get_ticks()
animation_cooldown = 50
frame = 0
last_attack_time = pygame.time.get_ticks()  
move_left = False
move_right = False

redhood_size = 3
image_sprite = list()

redhood = RedHood(dx=400, dy=400, scale=redhood_size)
clock = pygame.time.Clock()
run = True
# pygame.display.flip()
while run:
    canvas.fill(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                redhood.update_action(action='jump')
            if event.key == pygame.K_a:
                move_left = True        
                redhood.update_action(action='move')
            if event.key == pygame.K_d:
                move_right = True   
                redhood.update_action(action='move')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
                redhood.update_action(action='idle')
            if event.key == pygame.K_d:
                move_right = False
                redhood.update_action(action='idle')
            if event.key == pygame.K_SPACE and not redhood.jumping:
                redhood.update_action(action='idle')
                
    left_mouse, middle_mouse, right_mouse = pygame.mouse.get_pressed()
    if left_mouse:
        if pygame.time.get_ticks() - last_attack_time  <= redhood.combo_delay:
            redhood.combo_count += 1
            print(redhood.combo_count)
        else:
            redhood.combo_count = 0
            print('0')
            print(str(pygame.time.get_ticks() - redhood.time) + 'keje')
        last_attack_time = pygame.time.get_ticks()

    if redhood.combo_count >= redhood.combo_max:
        redhood.update_action(action="attack")

    redhood.update_animation()
    redhood.move(move_left=move_left, move_right=move_right)
    redhood.draw(canvas=canvas)

    pygame.display.update()
    clock.tick(60)
    
   