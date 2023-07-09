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
        self.jump_count = 10
        self.attacking = False
        self.combo_count = 0
        self.combo_max = 5
        self.combo_delay = 1000
        self.x = dx
        self.y = dy
        # action: 0 = idle, action: 1 = move
        self.action = 'idle'
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
        self.rect.center = (self.x, self.y)

    def move(self, move_left: bool, move_right: bool):
        if move_left:
            self.direction = True
        if move_right:
            self.direction = False


    def update_animation(self):
        print(self.action)
        animation_cooldown = 60
        self.image = self.image_sprite[self.action][self.frame_index]
        if self.action == 'jump':
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                print(self.jump_count)
                self.time = pygame.time.get_ticks()
                # self.frame_index += 1                                 
                self.jumping = True
                self.rect.y -= self.jump_count ** 2 * 0.5 * neg
                self.jump_count -= 1
            else:
                self.jump_count = 10
                self.jumping = False
                self.action = 'idle'

            if self.frame_index >= len(self.image_sprite[self.action]):
                self.jumping = False
                self.rect.y += 20
                self.update_action(action='idle')
        elif self.action == 'attack':
            print()
        else:
            if pygame.time.get_ticks() - self.time > animation_cooldown:
                self.time = pygame.time.get_ticks()
                self.frame_index += 1
            if self.frame_index >= len(self.image_sprite[self.action]):
                self.time = pygame.time.get_ticks()
                self.frame_index = 0


    def update_action(self, action):
        if self.action != action:
            if not self.jumping or not self.attacking:
                self.action = action
            self.frame_index = 0
                # self.time = pygame.time.get_ticks()


    def draw(self, canvas: object):
        canvas.blit(pygame.transform.flip(self.image, self.direction, False), self.rect)