import pygame

def main():
	pygame.init()
	screen = pygame.display.set_mode((720, 900))
	color = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
	i = 0
	dt = 0
	clock = pygame.time.Clock()
	player_pos = pygame.Vector2(100, screen.get_height() / 2)
	dead_pos = player_pos

	max_jump = 12
	on_cooldown = False
	cooldown_start = 0
	counter = 0
	acceleration = 1
	jumping = False
	dead = False

	background = pygame.image.load("flapPy-bird/bg_5.png")
	background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
	player = [pygame.image.load("flapPy-bird/Player_1.png"), pygame.image.load("flapPy-bird/Player_2.png"), pygame.image.load("flapPy-bird/Player_3.png")]
	dead_player = pygame.image.load("flapPy-bird/Dead.png")

	img = 0

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and not on_cooldown:
					jumping = True
					counter = 0
					cooldown_start = pygame.time.get_ticks()
				if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
					running = False

		screen.blit(background, (0, 0))
	
		if not dead:
			screen.blit(player[img], (player_pos.x, player_pos.y))
		else:
			screen.blit(dead_player, (dead_pos.x, dead_pos.y))
		
		img += 1
		if img > 2:
			img = 0

		if jumping and counter < max_jump and player_pos.y - 82 > 0:
			player_pos.y -= 1000 * dt
			counter += 1
			img = 1
		elif jumping and player_pos.y - 82 < 1:
			jumping = False
			counter = max_jump
		else:
			jumping = False

		if cooldown_start:
			on_cooldown = True
			cooldown_stop = pygame.time.get_ticks()
			if cooldown_stop - cooldown_start > 300:
				on_cooldown = False
				cooldown_start = 0
				cooldown_stop = 0

		if player_pos.y < screen.get_height() - 82:
			player_pos.y += 400 * dt

		if player_pos.y > screen.get_height() - 82:
			dead = True
			dead_pos.x = player_pos.x
			dead_pos.y = player_pos.y
		
		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == '__main__':
	main()