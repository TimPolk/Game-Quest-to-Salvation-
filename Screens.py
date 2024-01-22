import pygame


screen_length = 1500
screen_height = 1000
pygame.init()

timer = pygame.time.Clock()




def start_screen(screen):
    white_color = (250, 250, 250)
    black_color = (0, 0, 0)

    screen.fill(black_color)


    #game title letters
    title_font = pygame.font.SysFont("Minecraft", 150)
    title_surface = title_font.render("Quest to Salvation", 0, white_color)
    pygame.draw.rect(screen, white_color, (screen_length/2 - 500, screen_height/2 - 350, 1000, 200), width= 5)
    title_rectangle = title_surface.get_rect(center= (screen_length/2, screen_height/2 - 250))
    screen.blit(title_surface, title_rectangle)

    press_font = pygame.font.Font(None, 75)
    press_surface = press_font.render("Press to start", 0, white_color)
    press_rectangle = press_surface.get_rect(center=(screen_length / 2, screen_height / 2 + 100))
    press_button = screen.blit(press_surface, press_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if press_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Main Menu'

        pygame.display.update()
def main_menu(screen):
    white_color = (250, 250, 250)
    black_color = (0, 0, 0)

    screen.fill(black_color)
    #main menu letters
    main_menu_font = pygame.font.SysFont("Minecraft", 125)
    main_menu_surface = main_menu_font.render("Main Menu", 0, white_color)
    main_menu_rectangle = main_menu_surface.get_rect(center=(screen_length / 2, screen_height / 8))
    screen.blit(main_menu_surface, main_menu_rectangle)

    #side bar to choose options
    new_game_font = pygame.font.SysFont("Minecraft", 60)
    new_game_surface = new_game_font.render("New Game", 0, white_color)
    new_game_rectangle = new_game_surface.get_rect(center=(screen_length / 8 - 15, screen_height / 4))
    new_game_button = screen.blit(new_game_surface, new_game_rectangle)

    load_game_font = pygame.font.SysFont("Minecraft", 60)
    load_game_surface = load_game_font.render("Load Game", 0, white_color)
    load_game_rectangle = load_game_surface.get_rect(center=(screen_length / 8 - 10, screen_height / 4 + 100))
    load_game_button = screen.blit(load_game_surface, load_game_rectangle)

    settings_font = pygame.font.SysFont("Minecraft", 60)
    settings_surface = settings_font.render("Settings", 0, white_color)
    settings_rectangle = settings_surface.get_rect(center=(screen_length / 8 - 35, screen_height / 4 + 200))
    settings_button = screen.blit(settings_surface, settings_rectangle)

    quit_font = pygame.font.SysFont("Minecraft", 60)
    quit_surface = quit_font.render("Quit", 0, white_color)
    quit_rectangle = quit_surface.get_rect(center=(screen_length / 8 - 75, screen_height / 4 + 300))
    quit_button = screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_button.collidepoint(pygame.mouse.get_pos()):
                    return 'New Game'
                elif load_game_button.collidepoint(pygame.mouse.get_pos()):
                    return "Load Game"
                elif settings_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Settings'
                elif quit_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Quit'
        pygame.display.update()

def new_game(screen):
    white_color = (250, 250, 250)
    black_color = (0, 0, 0)

    screen.fill(black_color)

    new_game_font = pygame.font.SysFont("Minecraft", 125)
    new_game_surface = new_game_font.render("New Game", 0, white_color)
    new_game_rectangle = new_game_surface.get_rect(center=(screen_length / 2, screen_height / 8))
    screen.blit(new_game_surface, new_game_rectangle)
    # back button to go back to main menu
    back_font = pygame.font.SysFont("Minecraft", 60)
    back_surface = back_font.render("Back", 0, white_color)
    back_rectangle = back_surface.get_rect(center=(screen_length / 8 - 70, screen_height - 200))
    back_button = screen.blit(back_surface, back_rectangle)

    easy_font = pygame.font.SysFont("Minecraft", 75)
    easy_surface = easy_font.render("Easy", 0, white_color)
    easy_rectangle = easy_surface.get_rect(center=(screen_length / 8 - 70, screen_height / 2 - 200))
    easy_button = screen.blit(easy_surface, easy_rectangle)

    medium_font = pygame.font.SysFont("Minecraft", 75)
    medium_surface = medium_font.render("Medium", 0, white_color)
    medium_rectangle = medium_surface.get_rect(center=(screen_length / 8 - 35, screen_height / 2 - 100))
    medium_button = screen.blit(medium_surface, medium_rectangle)

    hard_font = pygame.font.SysFont("Minecraft", 75)
    hard_surface = hard_font.render("Hard", 0, white_color)
    hard_rectangle = hard_surface.get_rect(center=(screen_length / 8 - 70, screen_height / 2))
    hard_button = screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Main Menu'
                if easy_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Easy'
                if medium_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Medium'
                if hard_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Hard'
        pygame.display.update()

def load_game(screen):
    white_color = (250, 250, 250)
    black_color = (0, 0, 0)

    screen.fill(black_color)

    load_game_font = pygame.font.SysFont("Minecraft", 125)
    load_game_surface = load_game_font.render("Load Game", 0, white_color)
    load_game_rectangle = load_game_surface.get_rect(center=(screen_length / 2, screen_height / 8))
    screen.blit(load_game_surface, load_game_rectangle)
    # back button to go back to main menu
    back_font = pygame.font.SysFont("Minecraft", 60)
    back_surface = back_font.render("Back", 0, white_color)
    back_rectangle = back_surface.get_rect(center=(screen_length / 8 - 35, screen_height - 200))
    back_button = screen.blit(back_surface, back_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Main Menu'
        pygame.display.update()

def settings(screen):
    white_color = (250, 250, 250)
    black_color = (0, 0, 0)

    screen.fill(black_color)

    settings_font = pygame.font.SysFont("Minecraft", 125)
    settings_surface = settings_font.render("Settings", 0, white_color)
    settings_rectangle = settings_surface.get_rect(center=(screen_length / 2, screen_height / 8))
    screen.blit(settings_surface, settings_rectangle)
    #back button to go back to main menu
    back_font = pygame.font.SysFont("Minecraft", 60)
    back_surface = back_font.render("Back", 0, white_color)
    back_rectangle = back_surface.get_rect(center=(screen_length / 8 - 35, screen_height - 200))
    back_button = screen.blit(back_surface, back_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Main Menu'
        pygame.display.update()

def game_settings(screen):
    white_color = (250, 250, 250)
    black_color = (0, 0, 0)

    screen.fill(black_color)

    settings_font = pygame.font.SysFont("Minecraft", 125)
    settings_surface = settings_font.render("Settings", 0, white_color)
    settings_rectangle = settings_surface.get_rect(center=(screen_length / 2, screen_height / 8))
    screen.blit(settings_surface, settings_rectangle)
    #back button to go back to main menu
    back_font = pygame.font.SysFont("Minecraft", 60)
    back_surface = back_font.render("Back", 0, white_color)
    back_rectangle = back_surface.get_rect(center=(screen_length / 8 - 35, screen_height - 200))
    back_button = screen.blit(back_surface, back_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(pygame.mouse.get_pos()):
                    return 'Easy'
        pygame.display.update()
def dia_screen(screen, Text, difficulty):
    white_color = (250, 250, 250)
    black_color = (0, 0, 0)

    text_box_length = 1000
    text_box_height = 85

    screen.fill(black_color)
    #render the font of text
    text_font = pygame.font.Font(None, 40)
    #text box
    rect = (screen_length / 2 - 500, screen_height / 2 + 300, text_box_length, text_box_height)
    text_box = pygame.draw.rect(screen, white_color, rect, width=3)

    counter = 0
    speed = 1
    done = False
    run = True
    #the cool way text works
    while run:
        timer.tick(60)
        for event in pygame.event.get():
            if counter < speed * len(Text):
                counter += 1
            elif counter >= speed * len(Text):
                done = True
            snip = text_font.render(Text[0: counter//speed], False, white_color)
            screen.blit(snip, (rect[0] + 50, rect[1] + 25))
            pygame.display.flip()

            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #box for the paused menu
                    pygame.draw.rect(screen, white_color, (screen_length / 3 + 50, screen_height / 6, 400, 550), width=5)

                    #game paused letters
                    paused_font = pygame.font.Font(None, 65)
                    paused_surface = paused_font.render("Game Paused", 0, white_color)
                    paused_rectangle = paused_surface.get_rect(center=(screen_length / 3 + 250, screen_height / 6 + 50))
                    screen.blit(paused_surface, paused_rectangle)

                    #restart button
                    restart_font = pygame.font.Font(None, 55)
                    restart_surface = restart_font.render("Restart Game", 0, white_color)
                    restart_rectangle = restart_surface.get_rect(center=(screen_length / 3 + 250, screen_height / 6 + 175))
                    restart_button = screen.blit(restart_surface, restart_rectangle)

                    #settings_button
                    settings_font = pygame.font.Font(None, 55)
                    settings_surface = settings_font.render("Settings", 0, white_color)
                    settings_rectangle = settings_surface.get_rect(center=(screen_length / 3 + 250, screen_height / 6 + 275))
                    settings_button = screen.blit(settings_surface, settings_rectangle)

                    #quit game button
                    quit_font = pygame.font.Font(None, 55)
                    quit_surface = quit_font.render("Quit Game", 0, white_color)
                    quit_rectangle = quit_surface.get_rect(center=(screen_length / 3 + 250, screen_height / 6 + 375))
                    quit_button = screen.blit(quit_surface, quit_rectangle)
                    for action in pygame.event.get():
                        if action.type == pygame.MOUSEBUTTONDOWN:
                            if quit_button.collidepoint(pygame.mouse.get_pos()):
                                return "Quit"
                            elif settings_button.collidepoint(pygame.mouse.get_pos()):
                                return "Settings"
                            elif restart_button.collidepoint(pygame.mouse.get_pos()):
                                return difficulty

                        elif action.type == pygame.KEYDOWN:
                            if action.key == pygame.K_BACKSPACE:
                                return difficulty
                pygame.display.flip()
            