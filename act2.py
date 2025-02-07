#level up this game

import pygame
import random
from pygame import mixer   #add
  
mixer.init()   #add
   
s_color = "blue"
color = "orange"
class Sprite(pygame.sprite.Sprite):
	def __init__(self, color, height, width):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(s_color)
		pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
		self.rect = self.image.get_rect()

	def moveRight(self, pix):    #add
		self.rect.x += pix
	def moveLeft(self, pix):
		self.rect.x -= pix
	def moveForward(self, speed):
		self.rect.y += speed * speed/10
	def moveBack(self, speed):
		self.rect.y -= speed * speed/10

bg = pygame.image.load("bg.jpeg")   #add
bg = pygame.transform.scale(bg, (500, 500))   #add
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Level up game")
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
		elif event.type == pygame.KEYDOWN:  #add
			if event.key == pygame.K_x:
				exit = False

	keys = pygame.key.get_pressed()  #add
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
	screen.blit(bg,(0,0))  #add
	all_sprites_list.draw(screen)
	pygame.display.flip()

	if s1.rect.colliderect(s2.rect):   #add
		all_sprites_list.remove(s2)
		text = "Great Job!"
		font = pygame.font.SysFont("Times new Roman", 50)  
		text = font.render(text, True, (158, 16, 16))
		screen.blit(text,(200 - text.get_width() // 2, 140 - text.get_height() // 2))
		mixer.music.load("explosion.wav")  #opt
		mixer.music.set_volume(0.5)
		mixer.music.play()
		
	pygame.display.update()
	clock.tick(60)

pygame.quit()