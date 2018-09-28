import pygame,sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((630,630))
    pygame.display.set_caption("Tank War")

    background_image = pygame.image.load(r"../image/background.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background_image,(0,0))

        pygame








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