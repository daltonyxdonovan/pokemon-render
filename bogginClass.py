import pygame, sys
GREEN = (0,255,0)
count = 0
ticker = 0
ticker1 = 0

def load_image(name):
    image = pygame.image.load(name)
    return image

class Boggin(pygame.sprite.Sprite):
	def __init__(self, state):
		super().__init__()
		self.state = state
		self.images = []
		self.images.append(load_image('assets/poopPoke1.png').convert_alpha())
		self.images.append(load_image('assets/poopPoke2.png').convert_alpha())
		self.images.append(load_image('assets/poopPoke3.png').convert_alpha())
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 300, 150)

	def update(self):
		global count
		count += 1
		if count >= 15:
			self.index = self.index + 1
			count = 0
		if self.index > 2:
			self.index = 0
			
		self.image = self.images[self.index]
		if self.state == 0:
			self.defaultAnim()
		if self.state == 1:
			self.poopAnim()
		if self.state == 2:
			self.rangAnim()
		
	def rangAnim(self):
		global ticker
		ticker= 0
		if ticker == 0:
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.append(load_image('assets/poopPoke_pooparang1.png').convert_alpha())
			self.images.append(load_image('assets/poopPoke_pooparang2.png').convert_alpha())
			self.images.append(load_image('assets/poopPoke_pooparang3.png').convert_alpha())
			ticker = 1
	def poopAnim(self):
		global ticker1
		ticker1 = 0
		if ticker1 == 0:
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.append(load_image('assets/poopPoke_poop1.png').convert_alpha())
			self.images.append(load_image('assets/poopPoke_poop2.png').convert_alpha())
			self.images.append(load_image('assets/poopPoke_poop3.png').convert_alpha())
			ticker1 = 1
	def defaultAnim(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('assets/poopPoke1.png').convert_alpha())
		self.images.append(load_image('assets/poopPoke2.png').convert_alpha())
		self.images.append(load_image('assets/poopPoke3.png').convert_alpha())
		
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


