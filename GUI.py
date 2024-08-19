import pygame
import GameLogic

pygame.init()

screen_width, screen_height = 400, 500
screen = pygame.display.set_mode((screen_width, screen_height))

background_color = (96, 72, 88)
grid_color = (70, 60, 70)
border_color = (50, 40, 50)
text_color = (255, 255, 255)
button_border_color = (255, 255, 255)
error_message_color = (255, 0, 0)

font = pygame.font.SysFont('Arial', 50, bold=True)
button_font = pygame.font.SysFont('Arial', 20, bold=True)
input_font = pygame.font.SysFont('Arial', 40, bold=True)
result_font = pygame.font.SysFont('Arial', 30, bold=True)
error_font = pygame.font.SysFont('Arial', 20, bold=True)

rows, cols = 6, 5
cell_size = 50
cell_padding = 10
grid_x_offset = (screen_width - (cols * (cell_size + cell_padding))) // 2
grid_y_offset = 100
message_y_offset = grid_y_offset + (rows * (cell_size + cell_padding)) + 20

button_width, button_height = 50, 30
button_padding = 10
button_x = screen_width - button_width - 20
button_y_start = 20

max_attempts = 6

def reset_game():
    global current_row, current_col, current_input, attempts, game_over, game_result, all_attempts, wordToGuess, show_error_message
    current_row = 0
    current_col = 0
    current_input = ['' for _ in range(cols)]
    attempts = 0
    game_over = False
    game_result = ""
    all_attempts = []
    wordToGuess = GameLogic.SelectWord(current_language)
    show_error_message = False
    pygame.display.set_caption('WORDLE' if current_language == "EN" else 'TERMO')

def get_result_message():
    if current_language == "EN":
        return {
            "win": "You won!",
            "lose": f"The word was {wordToGuess}"
        }
    else:
        return {
            "win": "Você ganhou!",
            "lose": f"A palavra era: {wordToGuess}"
        }

def get_error_message():
    if current_language == "EN":
        return "This word does not exist"
    else:
        return "Essa palavra não existe"

def draw_grid():
    for row in range(rows):
        for col in range(cols):
            x = grid_x_offset + col * (cell_size + cell_padding)
            y = grid_y_offset + row * (cell_size + cell_padding)
            pygame.draw.rect(screen, grid_color, (x, y, cell_size, cell_size))
            pygame.draw.rect(screen, border_color, (x, y, cell_size, cell_size), 3)

def draw_attempts():
    for i, attempt in enumerate(all_attempts):
        for j in range(cols):
            x = grid_x_offset + j * (cell_size + cell_padding)
            y = grid_y_offset + i * (cell_size + cell_padding)
            color = grid_color  
            if j < len(attempt):
                result = attempt[j]['result']
                if result == 'right':
                    color = (58, 163, 148)  
                elif result == 'wrong_place':
                    color = (211, 173, 105)
                else:
                    color = (49, 42, 44) 
                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
                pygame.draw.rect(screen, border_color, (x, y, cell_size, cell_size), 3)
                if attempt[j]['letter'] != '':
                    text_surface = input_font.render(attempt[j]['letter'], True, text_color)
                    text_rect = text_surface.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
                    screen.blit(text_surface, text_rect)

def draw_input():
    if not game_over and current_row < rows:
        for i in range(cols):
            x = grid_x_offset + i * (cell_size + cell_padding)
            y = grid_y_offset + current_row * (cell_size + cell_padding)
            text_surface = input_font.render(current_input[i], True, text_color)
            text_rect = text_surface.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            screen.blit(text_surface, text_rect)

def draw_buttons():
    for button in buttons:
        pygame.draw.rect(screen, button_border_color, button["rect"], 2)
        label = button_font.render(button["label"], True, text_color)
        label_rect = label.get_rect(center=button["rect"].center)
        screen.blit(label, label_rect)

def draw_result():
    if game_over:
        result_message = get_result_message()
        result_text = result_font.render(result_message["win"] if game_result == "win" else result_message["lose"], True, text_color)
        result_rect = result_text.get_rect(center=(screen_width // 2, message_y_offset))
        screen.blit(result_text, result_rect)

def draw_error_message():
    if show_error_message:
        error_message = get_error_message()
        error_text = error_font.render(error_message, True, error_message_color)
        error_rect = error_text.get_rect(center=(screen_width // 2, message_y_offset - 40))
        screen.blit(error_text, error_rect)

def check_win_condition(rightIndices, wrongPlaceIndices, wrongIndices):
    return len(rightIndices) == cols and not wrongPlaceIndices and not wrongIndices

buttons = [
    {"label": "EN", "rect": pygame.Rect(button_x, button_y_start, button_width, button_height)},
    {"label": "PT", "rect": pygame.Rect(button_x, button_y_start + button_height + button_padding, button_width, button_height)}
]

current_language = "PT"
reset_game()

running = True
while running:
    screen.fill(background_color)
    title_text = font.render('WORDLE' if current_language == "EN" else 'TERMO', True, text_color)
    title_rect = title_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(title_text, title_rect)
    
    draw_grid()
    draw_attempts()
    draw_input()
    draw_buttons()
    draw_result()
    draw_error_message()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                if button["rect"].collidepoint(mouse_pos):
                    if button["label"] == "EN":
                        current_language = "EN"
                        reset_game()
                    elif button["label"] == "PT":
                        current_language = "PT"
                        reset_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if not game_over and current_col > 0:
                    current_col -= 1
                    current_input[current_col] = ''
            elif event.key == pygame.K_RETURN:
                if game_over:
                    reset_game()
                else:
                    guessWord = ''.join(current_input)
                    if len(guessWord) == cols:
                        if GameLogic.wordExist(guessWord, current_language):
                            rightIndices, wrongPlaceIndices, wrongIndices = GameLogic.wordVerification(guessWord, wordToGuess)
                            attempts += 1
                            
                            attempt_result = [
                                {
                                    'letter': current_input[j],
                                    'result': 'right' if j in rightIndices else
                                              'wrong_place' if j in wrongPlaceIndices else
                                              'wrong'
                                }
                                for j in range(cols)
                            ]
                            all_attempts.append(attempt_result)
                            
                            if check_win_condition(rightIndices, wrongPlaceIndices, wrongIndices):
                                game_result = "win"
                                game_over = True
                            elif attempts >= max_attempts:
                                game_result = "lose"
                                game_over = True
                            else:
                                current_row += 1
                                current_col = 0
                                current_input = ['' for _ in range(cols)]
                                
                            show_error_message = False
                        else:
                            show_error_message = True
                    else:
                        show_error_message = True
            elif event.key == pygame.K_RETURN and show_error_message:
                show_error_message = False
                current_input = ['' for _ in range(cols)]
                current_col = 0

            elif event.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f,
                               pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l,
                               pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r,
                               pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x,
                               pygame.K_y, pygame.K_z]:
                if not game_over and current_col < cols:
                    current_input[current_col] = pygame.key.name(event.key).upper()
                    current_col += 1

    pygame.display.flip()

pygame.quit()
