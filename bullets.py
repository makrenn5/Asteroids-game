from constants import *

from circleshape import *

class Shot(CircleShape):

	def __init__(self, x, y, SHOT_RADIUS):
		super().__init__(x, y, SHOT_RADIUS)

		for container in Shot.containers:
			container.add(self)


	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

	def update(self, dt):
		self.position += (self.velocity * dt)
		
