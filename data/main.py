import pygame,sys
import wall,myTank


def main():
    pygame.init()
    screen = pygame.display.set_mode((630,630))
    pygame.display.set_caption("Tank War")

    background_image = pygame.image.load(r"../resources/img/background.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background_image,(0,0))

        #定义精灵组
        myTankGroup = pygame.sprite.Group()

        #创建砖块
        bgMap = wall.Map()
        for each in bgMap.brickGroup:
            screen.blit(each.image, each.rect)


        #创建坦克
        myTank_T1 = myTank.MyTank()
        myTankGroup.add(myTank_T1)
        screen.blit(myTank_T1.tank_R0,(3,3))

        #屏幕刷新
        pygame.display.flip()

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        pygame.quit()
        input()