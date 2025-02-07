#block collision
import pygame
import random
  
s_color= "blue"
color = "orange"

class Sprite(pygame.sprite.Sprite):
	def __init__(self, color, height, width):
		super().__init__()

		self.image = pygame.Surface([width, height])
		self.image.fill(s_color)
		pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
		self.rect = self.image.get_rect()

	def moveRight(self, pixels):
		self.rect.x += pixels

	def moveLeft(self, pixels):
		self.rect.x -= pixels

	def moveForward(self, speed):
		self.rect.y += speed * speed/10

	def moveBack(self, speed):
		self.rect.y -= speed * speed/10
  
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Collision")

all_sprites_list = pygame.sprite.Group()

s1 = Sprite(color, 20, 30)
s1.rect.x = random.randint(0,480)
s1.rect.y = random.randint(0,480)
all_sprites_list.add(s1)


s2 = Sprite((255,0,0), 20, 30)   #add
s2.rect.x = random.randint(0,480)
s2.rect.y = random.randint(0,480)
all_sprites_list.add(s2)

rad=20   #add

exit = True
clock = pygame.time.Clock()
  
while exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				exit = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		s1.moveLeft(5)
	if keys[pygame.K_RIGHT]:
		s1.moveRight(5)
	if keys[pygame.K_DOWN]:
		s1.moveForward(5)
	if keys[pygame.K_UP]:
		s1.moveBack(5)

	all_sprites_list.update()
	screen.fill(s_color)
	all_sprites_list.draw(screen)
	pygame.display.flip()
	if s1.rect.colliderect(s2.rect):
		all_sprites_list.remove(s2)
		
	pygame.display.update()
	clock.tick(60)

pygame.quit()