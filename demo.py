

# Add sprite activity
import pygame
import random
from pygame import mixer
mixer.init()

#surf_color="pink"
color="blue"  
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image=pygame.Surface([w,h])
        #self.image.fill(surf_color)
        pygame.draw.rect(self.image, color, pygame.Rect(0,0,w,h))
        self.rect=self.image.get_rect()

    def moveRight(self,pix):
        self.rect.x +=pix
    def moveLeft(self,pix):
        self.rect.x -=pix
    def moveForward(self,speed):
        self.rect.y-=speed*speed/10
    def moveBackward(self,speed):
        self.rect.y+=speed*speed/10

bg=pygame.image.load("bg.jpeg")  
bg=pygame.transform.scale(bg,(500,500))    

pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Adding Sprite n collision")

sprite_list=pygame.sprite.Group()

s1=Sprite(color, 50,50)
s1.rect.x=random.randint(0,450)
s1.rect.y=random.randint(0,450)
sprite_list.add(s1)

s2=Sprite("orange", 50,50)
s2.rect.x=random.randint(0,450)
s2.rect.y=random.randint(0,450)
sprite_list.add(s2)

exit=True
clock=pygame.time.Clock()

rad=20

while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                exit=False
        
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        s1.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        s1.moveRight(5)
    if keys[pygame.K_UP]:
        s1.moveForward(5)
    if keys[pygame.K_DOWN]:
        s1.moveBackward(5)


    sprite_list.update()
    #screen.fill(surf_color)
    screen.blit(bg,(0,0))
    sprite_list.draw(screen)
    pygame.display.flip()

   

    if s1.rect.colliderect(s2.rect):
        sprite_list.remove(s2)
        text="game over"
        font=pygame.font.SysFont("Times new Roman", 50)
        text=font.render(text,True,(158,16,16))

        screen.blit(text,(200-text.get_width()//2, 150-text.get_height()//2))
        

    pygame.display.update()
    clock.tick(60)  #msec

pygame.quit()
