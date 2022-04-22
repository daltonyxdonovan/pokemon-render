import pygame, sys
GREEN = (0,255,0)
count = 0
count2 = 0
count3 = 0

def load_image(name):
    image = pygame.image.load(name)
    return image

class Slime(pygame.sprite.Sprite):
	def __init__(self, state):
		super().__init__()
		self.state = int(state)
		self.images = []
		self.images.append(load_image('assets/slimePoke1.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke2.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke3.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke4.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke5.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke6.png').convert_alpha())
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 300, 150)

	def update(self):
		global count
		count += 1
		if count >= 15:
			self.index = self.index + 1
			count = 0
		if self.index > 5:
			self.index = 0
			
		self.image = self.images[self.index]
		
		if self.state == 0:
			self.defaultAnim()
		if self.state == 1:
			self.slashAnim()
		if self.state == 2:
			self.acidAnim()
		
	def slashAnim(self):
		global count
		ticker1 = 0
		count = 15
		if ticker1 == 0:
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.append(load_image('assets/slimePoke_slash1.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash2.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash3.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash4.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash5.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash6.png').convert_alpha())
			ticker = 1
		else:
			self.images.append(load_image('assets/slimePoke_slash1.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash2.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash3.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash4.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash5.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_slash6.png').convert_alpha())
		
	def acidAnim(self):
		ticker = 0
		if ticker == 0:
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.pop(0)
			self.images.append(load_image('assets/slimePoke_acid1.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid2.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid3.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid4.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid5.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid6.png').convert_alpha())
			ticker = 1
		else:
			self.images.append(load_image('assets/slimePoke_acid1.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid2.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid3.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid4.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid5.png').convert_alpha())
			self.images.append(load_image('assets/slimePoke_acid6.png').convert_alpha())

	def defaultAnim(self):
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.pop(0)
		self.images.append(load_image('assets/slimePoke1.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke2.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke3.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke4.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke5.png').convert_alpha())
		self.images.append(load_image('assets/slimePoke6.png').convert_alpha())
		
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

