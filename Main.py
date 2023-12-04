import pygame
# import Character_Creation
screen_length = 1500
screen_height = 1000
pygame.init()
screen = pygame.display.set_mode((screen_length,screen_height))
pygame.display.set_caption("Quest to Salvation")

def start_screen(screen):
    white_color = (250, 250, 250)
    black_color = (0, 0, 0)

    screen.fill(black_color)



    title_font = pygame.font.SysFont("Minecreaft", 150)
    title_surface = title_font.render("Quest to Salvation", 0, white_color)
    pygame.draw.rect(screen, (250,250,250), (screen_length/2 - 500, screen_height/2 - 350, 1000, 200), width= 5)
    title_rectangle = title_surface.get_rect(center= (screen_length/2, screen_height/2 - 250))
    screen.blit(title_surface, title_rectangle)

    press_font = pygame.font.Font(None, 75)
    press_surface = press_font.render("Press to start", 0, white_color)
    press_rectangle = press_surface.get_rect(center=(screen_length / 2, screen_height / 2 + 100))
    screen.blit(press_surface, press_rectangle)

    pygame.display.update()
if __name__ == "__main__":
    pygame.font.get_fonts()
    start_screen(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()