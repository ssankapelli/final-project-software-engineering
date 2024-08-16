import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wandering in the Woods")

# Load and resize background image
background_image = pygame.image.load('background.png')
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load music and sounds
background_music = pygame.mixer.Sound('background_music.mp3')
movement_sound = pygame.mixer.Sound('movement.wav')
happy_sound = pygame.mixer.Sound('happy_sound.mp3')

# Load images
game_over_image = pygame.image.load('gameover.png')

# Play background music on home page
background_music.play(-1)

# Button dimensions
button_width = 200
button_height = 50

# Button positions
start_button_rect = pygame.Rect((SCREEN_WIDTH // 2) - (button_width // 2), (SCREEN_HEIGHT // 2) - (button_height // 2) - 50, button_width, button_height)
exit_button_rect = pygame.Rect((SCREEN_WIDTH // 2) - (button_width // 2), (SCREEN_HEIGHT // 2) - (button_height // 2) + 50, button_width, button_height)

# Exit button text
font = pygame.font.Font(None, 48)
exit_button_text = font.render('Exit', True, WHITE)

# Initialize grid size and characters
GRID_SIZE = (10, 10)  # Default value
characters = []
num_characters = 2

# Character class
class Character:
    def __init__(self, color, start_pos):
        self.color = color
        self.pos = start_pos
        self.moves = 0
        self.group = [self]  # Each character starts in its own group

    def move_randomly(self, grid_size):
        direction = random.choice(['up', 'down', 'left', 'right'])
        self.move(direction, grid_size)

    def move(self, direction, grid_size):
        if direction == 'up' and self.pos[1] > 0:
            self.pos[1] -= 1
        elif direction == 'down' and self.pos[1] < grid_size[1] - 1:
            self.pos[1] += 1
        elif direction == 'left' and self.pos[0] > 0:
            self.pos[0] -= 1
        elif direction == 'right' and self.pos[0] < grid_size[0] - 1:
            self.pos[0] += 1
        self.moves += 1

    def draw(self, cell_width, cell_height):
        rect = pygame.Rect(self.pos[0] * cell_width,
                           self.pos[1] * cell_height,
                           cell_width,
                           cell_height)
        pygame.draw.rect(screen, self.color, rect)

# def show_home_page():
#     screen.blit(background_image, (0, 0))
#     font = pygame.font.Font(None, 72)
#     title_text = font.render('Wandering in the Woods', True, '#53fa11')
#     start_button = pygame.draw.rect(screen, BLACK, start_button_rect)
#     exit_button = pygame.draw.rect(screen, BLACK, exit_button_rect)
#     screen.blit(title_text, (SCREEN_WIDTH // 6, SCREEN_HEIGHT // 8))
def show_home_page():
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 78)
    part1_text = font.render('Wandering', True, '#53fa11')
    part2_text = font.render('in the', True, '#0d2902')
    part3_text = font.render('Woods', True, '#53fa11')
    title_x = SCREEN_WIDTH // 8
    title_y = SCREEN_HEIGHT // 8
    screen.blit(part1_text, (title_x, title_y))
    screen.blit(part2_text, (title_x + part1_text.get_width() + 10, title_y))
    screen.blit(part3_text, (title_x + part1_text.get_width() + part2_text.get_width() + 20, title_y))


    start_button = pygame.draw.rect(screen, BLACK, start_button_rect)
    exit_button = pygame.draw.rect(screen, BLACK, exit_button_rect)
    start_button_text = font.render('Start', True, WHITE)
    exit_button_text = font.render('Exit', True, WHITE)
    screen.blit(start_button_text, (start_button_rect.x + 35 , start_button_rect.y + 3))
    screen.blit(exit_button_text, (exit_button_rect.x + 35, exit_button_rect.y + 3))
    pygame.display.flip()
    return start_button, exit_button

def show_game_over_screen(stats):
    screen.blit(background_image, (0, 0))
    screen.blit(game_over_image, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4))
    font = pygame.font.Font(None, 40)
    text2 = font.render(f'Shortest run: {stats["shortest_run"]:.2f}s', True, BLACK)
    screen.blit(text2, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 7))
    pygame.draw.rect(screen, BLACK, exit_button_rect)
    screen.blit(exit_button_text, (exit_button_rect.x + 40, exit_button_rect.y + 10))
    pygame.display.flip()




def configure_game():
    global GRID_SIZE, characters, num_characters

    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, 140, 32)
    grid_size_text = '10x10'
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    num_characters = 2
    num_char_button_rects = [
        pygame.Rect(SCREEN_WIDTH // 4 + i * 100, SCREEN_HEIGHT // 2, 80, 40)
        for i in range(3)
    ]
    num_char_buttons = ['2', '3', '4']

    running_config = True
    while running_config:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if 'x' in grid_size_text:
                        dimensions = grid_size_text.split('x')
                        try:
                            GRID_SIZE = (int(dimensions[0]), int(dimensions[1]))
                            print(f"Configured GRID_SIZE: {GRID_SIZE}")
                            running_config = False
                        except ValueError:
                            print("Invalid grid size format")
                elif event.key == pygame.K_BACKSPACE:
                    grid_size_text = grid_size_text[:-1]
                else:
                    grid_size_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
                for i, rect in enumerate(num_char_button_rects):
                    if rect.collidepoint(event.pos):
                        num_characters = int(num_char_buttons[i])
                        print(f"Configured number of characters: {num_characters}")

        screen.blit(background_image, (0, 0))
        txt_surface = font.render(grid_size_text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        for i, rect in enumerate(num_char_button_rects):
            pygame.draw.rect(screen, BLACK, rect)
            button_text = font.render(num_char_buttons[i], True, WHITE)
            screen.blit(button_text, (rect.x + 20, rect.y + 10))

        pygame.display.flip()

    characters = []
    for _ in range(num_characters):
        x = random.randint(0, GRID_SIZE[0] - 1)
        y = random.randint(0, GRID_SIZE[1] - 1)
        color = RED if len(characters) == 0 else (BLUE if len(characters) == 1 else (GREEN if len(characters) == 2 else YELLOW)) 
        characters.append(Character(color, [x, y]))
    print(f"Characters initialized: {characters}")

def main_game_loop():
    global GRID_SIZE, characters, num_characters

    stats = {
        'longest_run': 0,
        'shortest_run': float('inf'),
        'total_runs': 0,
        'run_count': 0,
        'average_run': 0,
    }

    game_over = False
    start_time = pygame.time.get_ticks()

    cell_width = SCREEN_WIDTH // GRID_SIZE[0]
    cell_height = SCREEN_HEIGHT // GRID_SIZE[1]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_UP:
                    for char in characters[0].group:
                        char.move('up', GRID_SIZE)
                    movement_sound.play()
                elif event.key == pygame.K_DOWN:
                    for char in characters[0].group:
                        char.move('down', GRID_SIZE)
                    movement_sound.play()
                elif event.key == pygame.K_LEFT:
                    for char in characters[0].group:
                        char.move('left', GRID_SIZE)
                    movement_sound.play()
                elif event.key == pygame.K_RIGHT:
                    for char in characters[0].group:
                        char.move('right', GRID_SIZE)
                    movement_sound.play()
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                if exit_button_rect.collidepoint(event.pos):
                    return

        if not game_over:
            for i in range(1, num_characters):
                if len(characters[i].group) == 1:
                    characters[i].move_randomly(GRID_SIZE)
            positions = [char.pos for char in characters]
            unique_positions = set(tuple(pos) for pos in positions)
            if len(unique_positions) < len(positions):
                for char in characters:
                    for other_char in characters:
                        if char != other_char and char.pos == other_char.pos and other_char not in char.group:
                            char.group.extend(other_char.group)
                            for c in other_char.group:
                                c.group = char.group

                all_in_same_group = all(char.group == characters[0].group for char in characters)
                if all_in_same_group:
                    end_time = pygame.time.get_ticks()
                    run_duration = (end_time - start_time) / 1000
                    stats['total_runs'] += run_duration
                    stats['run_count'] += 1
                    stats['longest_run'] = max(stats['longest_run'], run_duration)
                    stats['shortest_run'] = min(stats['shortest_run'], run_duration)
                    stats['average_run'] = stats['total_runs'] / stats['run_count']
                    happy_sound.play()
                    game_over = True

            screen.blit(background_image, (0, 0))
            for char in characters:
                char.draw(cell_width, cell_height)
            pygame.display.flip()

            pygame.time.wait(500)

        if game_over:
            show_game_over_screen(stats)

def main():
    start_button, exit_button = show_home_page()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    background_music.stop()
                    configure_game()
                    main_game_loop()
                    start_button, exit_button = show_home_page()
                    background_music.play(-1)
                elif exit_button.collidepoint(event.pos):
                    running = False

    pygame.quit()

if __name__ == "__main__":
    main()
