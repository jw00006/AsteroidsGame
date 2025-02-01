import pygame
from constants import *
from player import Player

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	bg_color = (0, 0, 0) #BLACK
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	#game loop
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		pygame.Surface.fill(screen, bg_color)
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		

if __name__ == "__main__":
	main()

