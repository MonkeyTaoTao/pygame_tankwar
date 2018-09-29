import pygame

tankImg= r"../resources/img/tank_T1_0.png"

class MyTank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #载入图片
        self.tank = pygame.image.load(tankImg)
        #截取图片
        self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))

        self.rect = self.tank.get_rect()
        self.speed = 4

    def moveUp(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * -1)
        self.tank_R0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 0), (48, 48))
        self.dir_x, self.dir_y = 0, -1
        if self.rect.top < 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * 1)
            return True
        return False

    def moveDown(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 0, self.speed * 1)
        self.tank_R0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 48), (48, 48))
        self.dir_x, self.dir_y = 0, 1
        if self.rect.bottom > 630 - 3:
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 0, self.speed * -1)
            return True
        return False

    def moveLeft(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * -1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 96), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 96), (48, 48))
        self.dir_x, self.dir_y = -1, 0
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * 1, self.speed * 0)
            return True
        return False

    def moveRight(self, tankGroup, brickGroup, ironGroup):
        self.rect = self.rect.move(self.speed * 1, self.speed * 0)
        self.tank_R0 = self.tank.subsurface((0, 144), (48, 48))
        self.tank_R1 = self.tank.subsurface((48, 144), (48, 48))
        self.dir_x, self.dir_y = 1, 0
        if self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -1, self.speed * 0)
            return True
        return False