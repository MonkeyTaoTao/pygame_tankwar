import pygame

brickIMG = r"../resources/img/brick.png"
ironIMG = r"../resources/img/iron.png"

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(brickIMG)
        self.rect = self.image.get_rect()

class Iron(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(ironIMG)
        self.rect = self.image.get_rect()

class Map():
    def __init__(self):
        self.brickGroup = pygame.sprite.Group()
        self.ironGroup = pygame.sprite.Group()

        #画地图
        #将630*630的地图，按照砖块的大小划分，（630-3*2$地图边缘不可用像素$）/24 = 26 (共分为26行，26列）
        # 通过一位数组的方式构造地图
        # H1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        # L1 = [0, 1, 2, 3, 4]
        # 通过二维数组的形式构造地图
        X0Y0 = [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]
        for x,y in X0Y0:
            self.brick = Brick()
            self.brick.rect.left,self.brick.rect.top = 3 + x * 24,3 + y * 24
            self.brickGroup.add(self.brick)