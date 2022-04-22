import pygame, sys
GREEN = (0,255,0)
count = 0
count2 = 0
count3 = 0

def load_image(name):
    image = pygame.image.load(name)
    return image

class boxy(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.images = []
		self.images.append(load_image('assets/inputbox1.png').convert_alpha())
		self.images.append(load_image('assets/inputbox2.png').convert_alpha())

		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 250, 100)

	def update(self):
		global count
		count += 1
		if count >= 35:
			self.index = self.index + 1
			count = 0
		if self.index > 1:
			self.index = 0
			
		self.image = self.images[self.index]
		
def main():
	pygame.init()
	screen = pygame.display.set_mode((1000, 800))
	my_sprite = TestSprite()
	my_group = pygame.sprite.Group(my_sprite)
	
	while True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)

		# Calling the 'my_group.update' function calls the 'update' function of all 
		# its member sprites. Calling the 'my_group.draw' function uses the 'image'
		# and 'rect' attributes of its member sprites to draw the sprite.
		my_group.update()
		my_group.draw(screen)
		pygame.display.flip()

		

	if __name__ == '__main__':
		main()


