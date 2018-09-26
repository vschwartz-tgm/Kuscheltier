
import pygame


def main():

    pygame.init()
    pygame.display.set_mode((200, 100))
    pygame.mixer.music.load('D:\Diplomarbeit\Github\Kuscheltier\Teddy\Einleitung_Hallo2.wav')
    pygame.mixer.music.play(0)

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)

if __name__ == "__main__":
    main()