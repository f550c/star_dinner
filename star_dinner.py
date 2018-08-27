import pygame, sys
import random
from pygame.locals import *

pygame.init()

FPS = 50 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 550), 0, 32)
pygame.display.set_caption('star dinner')
GREEN = (0, 255, 0)
RED = (255, 0, 0)
fontObj = pygame.font.Font('freesansbold.ttf', 32)

WHITE = (255, 255, 255)
catImg = pygame.image.load('car.png')
obs=pygame.image.load('obs.png')
obs1=pygame.image.load('obs.png')
obs2=pygame.image.load('obs.png')
plus=pygame.image.load('plus.jpg')
road=pygame.image.load('road.png')
rpx=random.randint(100,500)
r1=random.randint(100,500)
r2=random.randint(100,500)
r3=random.randint(100,500)
obsx = 800+r1
obs1x = 1200+r2
obs2x = 1400+r3
rand1=random.randint(0,1)
rand2=random.randint(0,1)
rand3=random.randint(0,1)
	
if(rand1==0):
	obsy=280
	rpy=280
else:
	obsy=190
	rpy=190

if(rand2==0):
	obs1y=280
else:
	obs1y=190
if(rand3==0):
	obs2y=280
else:
	obs2y=190
carx=0
cary=280
direction = 'right'
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
lvl=0
spd=7
score=0
lives=5
while True: # the main game loop
	DISPLAYSURF.fill(WHITE)
	rand1=random.randint(0,1)
	rand2=random.randint(0,1)
	rand3=random.randint(0,1)
	
	textSurfaceObj = fontObj.render('SCORE='+str(score), True, GREEN,WHITE)
	textSurfaceObj1 = fontObj.render('LIVES='+str(lives), True, RED,WHITE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj1 = textSurfaceObj.get_rect()

	textRectObj.center = (200, 150)

	textRectObj1.center = (200, 50)


	if direction == 'right':
		spd=(score/5)+5
		obsx -= spd
		obs1x -= spd
		obs2x -= spd
		rpx -= spd+2
		if (rpx < 0):
			if(cary==rpy):
				score+=1
			rpx=800+r3
			if(rand1==0):
				rpy=280
				#obsy=280
			else:
				rpy=190
			if((obsx-obs1x)<300):
				rpx=obs2x+r3+r2+10
		if (obsx < 0):
			if(cary==obsy):
				lives-=1
			obsx=800+r3
			if(rand1==0):
				obsy=280
			else:
				obsy=190
			if((obsx-obs1x)<300):
				obsx=obs2x+r1+80
		if (obs1x < 0):
			if(cary==obs1y):
				lives-=1
			obs1x=800+r1
			if(rand2==0):
				obs1y=280+5
			else:
				obs1y=190
			if((obs1x-obs2x)<300):
				obs1x=obsx+r3-100
		if (obs2x < 0):
			if(cary==obs2y):
				lives-=1
			obs2x=800+r3
			if(rand3==0):
				obs2y=280
			else:
				obs2y=190
			if((obs2x-obsx)<300):
				obs2x=obs2x+200+r3
	DISPLAYSURF.blit(road,(0,0))
	DISPLAYSURF.blit(catImg, (carx, cary))
	DISPLAYSURF.blit(obs, (obsx, obsy))
	DISPLAYSURF.blit(obs1, (obs1x, obs1y))
	DISPLAYSURF.blit(obs2, (obs2x, obs2y))
	DISPLAYSURF.blit(plus, (rpx, rpy))
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	DISPLAYSURF.blit(textSurfaceObj1, textRectObj1)
	if (lives==-1):
		print("your score is :"+str(score))
		pygame.quit()
		sys.exit()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if (event.key == K_UP or event.key == K_w):
				cary=190
			if (event.key == K_DOWN or event.key == K_s):
				cary=280

	pygame.display.update()
	fpsClock.tick(FPS)
