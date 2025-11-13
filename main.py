import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from circleshape import CircleShape
from player import Player



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    spaceship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        spaceship.draw(screen)
        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.get_time() / 1000


if __name__ == "__main__":
    main()
