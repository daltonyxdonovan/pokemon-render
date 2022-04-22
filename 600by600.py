#imports
import time, random, sys, pygame, threading
from slimeClass import Slime
from bogginClass import Boggin
from inputbox import boxy

#inits
pygame.init()
screen = pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()

def slash():
	slashticker = 1
	turn = 1
	
	
def acid():
	acidticker = 1
	turn = 1
	acid.cancel()

def slashAttack():
	animState = 1

#colors
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
BGCOLOR = (255,236,231)

#variables
slash = threading.Timer(2.0, slash)
acid = threading.Timer(2.0, acid)
playername ='slimey       lvl5'
enemyname = 'poopin       lvl5'
playercolor = GREEN
enemycolor = GREEN
playerhealth = 400
enemyhealth = 400
running = True
myfont = pygame.font.Font("thick pixel.ttf", 14, bold=True)
topleft = True
topright = False
bottomleft = False
bottomright = False
slashticker = 0
acidticker = 0
turn = 0
playeratk = 0
enemyatk = 0

animState = 0
enemyanimState = 0

#sprite properties
Slimey = Slime(animState)
Slimey.rect.x = 50
Slimey.rect.y = 280

Poopin = Boggin(int(enemyanimState))
Poopin.rect.x = 560
Poopin.rect.y = 120

box = boxy()
box.rect.x = 500
box.rect.y = 450

#add sprites
allsprites = pygame.sprite.Group()
allsprites.add(Slimey)
allsprites.add(Poopin)
allsprites.add(box)

#main loop
while running:
	if playerhealth <= 0:
		exit()
	if enemyhealth <= 0:
		exit()
	screen.fill([255,236,231])
	
#rectangle logic
	pygame.draw.rect(screen, BLACK, [48, 448, 402, 27], 6)
	pygame.draw.rect(screen, playercolor, [50, 450, playerhealth, 25])
	pygame.draw.rect(screen, BLACK, [548, 28, 402, 27], 6)
	pygame.draw.rect(screen, enemycolor, [550, 30, enemyhealth, 25])
	pygame.draw.rect(screen, BLACK, [500, 450, 450, 200], 6)

#text properties
	playernametext = myfont.render(playername, 5, [0,0,0])	
	enemynametext = myfont.render(enemyname, 5, [0,0,0])
	slashtext = myfont.render("slash", 5, [0,0,0])
	acidtext = myfont.render("acid", 5, [0,0,0])
	itemtext = myfont.render("items", 5, [0,0,0])
	runtext = myfont.render("run",5,[0,0,0])
	
#text blits
	screen.blit(slashtext, [550, 480])
	screen.blit(acidtext, [770, 480])
	screen.blit(itemtext, [760, 570])
	screen.blit(runtext, [570, 570])
	screen.blit(enemynametext, [550, 60])
	screen.blit(playernametext, [50, 480])
	
#key inputs	
	keys = pygame.key.get_pressed()
	if turn == 0:
		enemyanimState = 0
		enemyatk = 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit(-1)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					exit(-1)
				if event.key == pygame.K_RETURN and topleft == True:
					Slimey.slashAnim()
					enemyhealth = enemyhealth - random.randrange(1,80,1)
					turn = 1
						
				if event.key == pygame.K_RETURN and topright == True:
					animState = 2
					
				if event.key == pygame.K_RETURN and bottomleft == True:
					exit()
						
	#topleft logic
				if event.key == pygame.K_RIGHT and topleft == True:
					topleft = False
					topright = True				
				if event.key == pygame.K_DOWN and topleft == True:
					topleft = False
					bottomleft = True
					
	#topright logic				
				if event.key == pygame.K_LEFT and topright == True:
					topright = False
					topleft = True				
				if event.key == pygame.K_DOWN and topright == True:
					topright = False
					bottomright = True
					
	#bottomleft logic				
				if event.key == pygame.K_RIGHT and bottomleft == True:
					bottomleft = False
					bottomright = True				
				if event.key == pygame.K_UP and bottomleft == True:
					bottomleft = False
					topleft = True
					
	#bottomright logic										
				if event.key == pygame.K_UP and bottomright == True:
					bottomright = False
					topright = True				
				if event.key == pygame.K_LEFT and bottomright == True:
					bottomright = False
					bottomleft = True
	if turn == 1:
		animState = 0
		if enemyatk == 0:
			enemychoice = random.randrange(1,3,1)
			if enemychoice == 1:
				Poopin.poopAnim()
				playerhealth = playerhealth - random.randrange(1,50,1)
				enemyatk = enemyatk + 1
				turn = 0
			if enemychoice == 2:
				Poopin.rangAnim()
				playerhealth = playerhealth - random.randrange(1,100,1)
				enemyatk = enemyatk + 1
				turn = 0
			
#choices shit			
	if topright:
		box.rect.x = 705 #topright
		box.rect.y = 450	
	if topleft:
		box.rect.x = 500 #topleft
		box.rect.y = 450	
	if bottomright:
		box.rect.x = 705 #bottomright
		box.rect.y = 550
	if bottomleft:
		box.rect.x = 500 #bottomleft
		box.rect.y = 550
		
#health bars
	if playerhealth < 200 and playerhealth > 100:
		playercolor = YELLOW
	if playerhealth < 100:
		playercolor = RED
	if enemyhealth < 200 and enemyhealth > 100:
		enemycolor = YELLOW
	if enemyhealth < 100:
		enemycolor = RED

#update cycle/ ticks		
	allsprites.update()
	allsprites.draw(screen)
	pygame.display.update()
	clock.tick(60)
