import pygame
# import Character_Creation
import Screens as GS
screen_length = 1500
screen_height = 1000
pygame.init()
screen = pygame.display.set_mode((screen_length,screen_height))
pygame.display.set_caption("Quest to Salvation")

#story elements here
kingdom = 'Pregon'
if __name__ == "__main__":

    # pygame.font.get_fonts()
    update = 'Start Screen'

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif update == 'Start Screen':
                update = GS.start_screen(screen)
            elif update == 'Main Menu':
                update = GS.main_menu(screen)
            elif update == 'New Game':
                update = GS.new_game(screen)
            elif update == 'Load Game':
                update = GS.load_game(screen)
            elif update == 'Settings':
                update = GS.settings(screen)

                #easy mode game starts from here
            elif update == 'Easy':
                difficulty = "Easy"
                Text = f"Welcome new hero, to the {kingdom} Kingdom!"
                update = GS.dia_screen(screen, Text, difficulty)

                #medium mode game starts from here
            elif update == 'Medium':
                difficulty = "Medium"
                Text = f"Welcome new hero, to the {kingdom} Kingdom!"
                update = GS.dia_screen(screen, Text,difficulty)

                #hard mode game starts from here
            elif update == 'Hard':
                difficulty = "Hard"
                Text = f"Welcome new hero, to the {kingdom} Kingdom!"
                update = GS.dia_screen(screen, Text, difficulty)

            elif update == 'Quit':
                running = False
        pygame.display.update()