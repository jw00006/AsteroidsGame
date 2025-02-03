import pygame
from constants import *
from player import Player
from asteroid import Asteroid

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	bg_color = (0, 0, 0) #BLACK

	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	updatable.add(player)
	drawable.add(player)
	#game loop
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		pygame.Surface.fill(screen, bg_color)
		dt = clock.tick(60) / 1000
		updatable.update(dt)
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()


if __name__ == "__main__":
	main()

