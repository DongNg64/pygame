import pygame
import os

class RedHood(pygame.sprite.Sprite):
    def __init__(self, dx: int, dy: int, scale: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.direction = False
        self.frame_index = 0
        self.image_sprite = dict()
        self.time = pygame.time.get_ticks()
        self.jumping = False
        self.attacking = False
        self.click = 0
        # action: 0 = idle, action: 1 = move
        self.action = 'idle'
        # self.scale = scale
        dir = './character/redhood/'
        animation_type = ['idle', 'move', 'jump', 'attack']
        for type in animation_type:
            amount_file_move = len(os.listdir(f'{dir}{type}'))
            temp_list = list()
            for index in range(amount_file_move):
                redhood = pygame.image.load(f'./character/redhood/{type}/{type}_{index}.png')
                redhood = pygame.transform.scale(redhood, (int(redhood.get_width() * scale), int(redhood.get_height() * scale)))
                temp_list.append(redhood)
            self.image_sprite.update({type: temp_list})

        self.image = self.image_sprite[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (dx, dy)

    # def check_out_of_move(self, frame_index):
        

    def move(self, move_left: bool, move_right: bool):
        if move_left:
            self.direction = True
        if move_right:
            self.direction = False


    def update_animation(self):
        animation_cooldown = 60
        self.image = self.image_sprite[self.action][self.frame_index]
        if self.action == 'jump':
            if pygame.time.get_ticks() - self.time > animation_cooldown:
                self.time = pygame.time.get_ticks()
                self.frame_index += 1
                self.jumping = True
                self.attacking = True
            if self.frame_index >= len(self.image_sprite[self.action]):
                self.jumping = False
                self.attacking = True
                self.update_action(action='idle')
        elif self.action == 'attack':
            if pygame.time.get_ticks() - self.time > 20:
                self.time = pygame.time.get_ticks()
                self.frame_index += 1
                self.attacking = True
            if self.frame_index >= 5 and self.click == 1:
                if pygame.time.get_ticks() - self.time < 500:
                    self.frame_index = 5
                self.attacking = False
                self.update_action(action='idle')
            elif self.frame_index >= 10 and self.click == 2:
                if pygame.time.get_ticks() - self.time < 500:
                    self.frame_index = 10
                self.attacking = False
                self.update_action(action='idle')
            elif self.frame_index >= len(self.image_sprite[self.action]) and self.click == 3:
                self.attacking = False
                self.update_action(action='idle')
        else:
            if pygame.time.get_ticks() - self.time > animation_cooldown:
                self.time = pygame.time.get_ticks()
                self.frame_index += 1
                # self.jumping = True
            if self.frame_index >= len(self.image_sprite[self.action]):
            # self.finish_action = True
                self.time = pygame.time.get_ticks()
                self.frame_index = 0

    def update_action(self, action):
        if self.action != action:
            if not self.jumping or not self.attacking:
                # self.update_animation()
                # if not self.fisnish_action:
                #     return
                self.action = action
                self.frame_index = 0
                self.time = pygame.time.get_ticks()
                # self.finish_action = False
            # else:
            #     self.action = action
            #     self.frame_index = 0
            #     self.time = pygame.time.get_ticks()

    def draw(self, canvas: object):
        print(self.click)
        canvas.blit(pygame.transform.flip(self.image, self.direction, False), self.rect)