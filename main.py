import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	bg_color = (0, 0, 0) #BLACK

	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	pygame.init()
	font = pygame.font.SysFont(None, 24)

	running = True
	state = "PLAY"
	score = 0
	final_score = 0
	def draw_score(screen, score):
		scoring = font.render(f"Score: {score}", True, (255, 255, 255))
		screen.blit(scoring, (10, 10))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	updatable.add(player)
	drawable.add(player)

	asteroid_field = AsteroidField()

	#game loop
	while running:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			running = False
		if state == "PLAY":
			pygame.Surface.fill(screen, bg_color)
			dt = clock.tick(60) / 1000
			updatable.update(dt)
			for obj in drawable:
				obj.draw(screen)
			draw_score(screen, score)
			for asteroid in asteroids:
				for shot in shots:
					if shot.collision_check(asteroid):
						shot.kill()
						asteroid.split()
						score += 50
				if player.collision_check(asteroid):
					final_score = score
					state = "GAME_OVER"


		elif state == "GAME_OVER":
			screen.fill((0,0,0))
			# display "game over" text
			over_text = font.render("Game over!", True, (255, 255, 255))
			screen.blit(over_text, (SCREEN_WIDTH/2 -50, SCREEN_HEIGHT/2 - 10))

			# display final score text
			final_score_text = font.render(f"Final score: {final_score}", True, (255, 255, 255))
			screen.blit(final_score_text, (SCREEN_WIDTH/2 -60, SCREEN_HEIGHT/2 + 10))

			# restart / exit commands
			instructions = font.render("Press R to restart, ESC to exit", True, (255, 255, 255))
			screen.blit(instructions, (SCREEN_WIDTH/2 -120, SCREEN_HEIGHT/2 +30))

			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				running = False
			if keys[pygame.K_r]:
				# reset score on restart
				score = 0
				state = "PLAY"

		pygame.display.flip()


if __name__ == "__main__":
	main()

