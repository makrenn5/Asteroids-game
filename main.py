import pygame

from constants import *

from player import *

from asteroid import *

from asteroidfield import *

from bullets import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
	incoming = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")

		for sprite in drawable:
			sprite.draw(screen)

		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collision_detect(player) == True:
				raise SystemExit("Game over!")
			
			for shot in shots:
				if asteroid.collision_detect(shot):
					shot.kill()
					asteroid.split()
		
		pygame.display.flip()

		clock.tick(60)

		dt = clock.tick(60) / 1000



if __name__ == "__main__":
		main() 


