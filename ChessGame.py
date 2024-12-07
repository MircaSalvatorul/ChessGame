# two player chess in python with Pygame!
# part one, set up variables images and game loop

import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 700
square_size = HEIGHT // 9
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60
# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []
# 0 - whites turn no selection: 1-whites turn piece selected: 2- black turn no selection, 3 - black turn piece selected
turn_step = 0
selection = 100
valid_moves = []
# load in game piece images (queen, king, rook, bishop, knight, pawn) x 2
black_queen = pygame.image.load('assets/images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (square_size * 0.8, square_size * 0.8))
black_queen_small = pygame.transform.scale(black_queen, (square_size * 0.4, square_size * 0.4))
black_king = pygame.image.load('assets/images/black king.png')
black_king = pygame.transform.scale(black_king, (square_size * 0.8, square_size * 0.8))
black_king_small = pygame.transform.scale(black_king, (square_size * 0.4, square_size * 0.4))
black_rook = pygame.image.load('assets/images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (square_size * 0.8, square_size * 0.8))
black_rook_small = pygame.transform.scale(black_rook, (square_size * 0.4, square_size * 0.4))
black_bishop = pygame.image.load('assets/images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (square_size * 0.8, square_size * 0.8))
black_bishop_small = pygame.transform.scale(black_bishop, (square_size * 0.4, square_size * 0.4))
black_knight = pygame.image.load('assets/images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (square_size * 0.8, square_size * 0.8))
black_knight_small = pygame.transform.scale(black_knight, (square_size * 0.4, square_size * 0.4))
black_pawn = pygame.image.load('assets/images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (square_size * 0.8, square_size * 0.8))
black_pawn_small = pygame.transform.scale(black_pawn, (square_size * 0.4, square_size * 0.4))
white_queen = pygame.image.load('assets/images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (square_size * 0.8, square_size * 0.8))
white_queen_small = pygame.transform.scale(white_queen, (square_size * 0.4, square_size * 0.4))
white_king = pygame.image.load('assets/images/white king.png')
white_king = pygame.transform.scale(white_king, (square_size * 0.8, square_size * 0.8))
white_king_small = pygame.transform.scale(white_king, (square_size * 0.4, square_size * 0.4))
white_rook = pygame.image.load('assets/images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (square_size * 0.8, square_size * 0.8))
white_rook_small = pygame.transform.scale(white_rook, (square_size * 0.4, square_size * 0.4))
white_bishop = pygame.image.load('assets/images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (square_size * 0.8, square_size * 0.8))
white_bishop_small = pygame.transform.scale(white_bishop, (square_size * 0.4, square_size * 0.4))
white_knight = pygame.image.load('assets/images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (square_size * 0.8, square_size * 0.8))
white_knight_small = pygame.transform.scale(white_knight, (square_size * 0.4, square_size * 0.4))
white_pawn = pygame.image.load('assets/images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (square_size * 0.8, square_size * 0.8))
white_pawn_small = pygame.transform.scale(white_pawn, (square_size * 0.4, square_size * 0.4))
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small,
                      white_rook_small, white_bishop_small]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small,
                      black_rook_small, black_bishop_small]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# draw main game board
def draw_board():
    # Draw 8x8 grid
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = 'light gray'
            else:
                color = 'gray'
            pygame.draw.rect(screen, color,
                             (col * square_size, row * square_size, square_size, square_size))

    # Draw UI elements below the board
    pygame.draw.rect(screen, 'gray', [0, 8 * square_size, WIDTH, HEIGHT - 8 * square_size])
    pygame.draw.rect(screen, 'gold', [0, 8 * square_size, WIDTH, HEIGHT - 8 * square_size], 5)
    pygame.draw.rect(screen, 'gold', [8 * square_size, 0, WIDTH - 8 * square_size, HEIGHT], 5)

    # Dynamically adjust font size to fit the status rectangle
    available_height = HEIGHT - 8 * square_size
    dynamic_font_size = int(available_height * 0.4)  # 40% of available height
    dynamic_font = pygame.font.Font('freesansbold.ttf', dynamic_font_size)

    # Display status text
    status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                   'Black: Select a Piece to Move!', 'Black: Select a Destination!']
    status_surface = dynamic_font.render(status_text[turn_step], True, 'black')
    status_rect = status_surface.get_rect(center=(WIDTH // 4, 8 * square_size + available_height // 2))
    screen.blit(status_surface, status_rect)

    # Draw vertical and horizontal lines for grid
    for i in range(9):
        pygame.draw.line(screen, 'black', (0, square_size * i), (8 * square_size, square_size * i), 2)
        pygame.draw.line(screen, 'black', (square_size * i, 0), (square_size * i, 8 * square_size), 2)

    # FORFEIT button
    forfeit_font = pygame.font.Font('freesansbold.ttf', dynamic_font_size)  # Smaller for the button
    forfeit_surface = forfeit_font.render('FORFEIT', True, 'black')
    forfeit_rect = forfeit_surface.get_rect(center=(9 * square_size, 8.5 * square_size))
    screen.blit(forfeit_surface, forfeit_rect)

# draw pieces onto board


def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        x, y = white_locations[i]
        piece_image = pygame.transform.scale(white_images[index], (square_size * 0.8, square_size * 0.8))
        screen.blit(piece_image,
                    (x * square_size + square_size * 0.1, y * square_size + square_size * 0.1))
        if turn_step < 2 and selection == i:
            pygame.draw.rect(screen, 'red',
                             [x * square_size + 1, y * square_size + 1, square_size - 2, square_size - 2], 2)

    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        x, y = black_locations[i]
        piece_image = pygame.transform.scale(black_images[index], (square_size * 0.8, square_size * 0.8))
        screen.blit(piece_image,
                    (x * square_size + square_size * 0.1, y * square_size + square_size * 0.1))
        if turn_step >= 2 and selection == i:
            pygame.draw.rect(screen, 'blue',
                             [x * square_size + 1, y * square_size + 1, square_size - 2, square_size - 2], 2)


# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


# check valid knight moves
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# draw valid moves on screen
def draw_valid(moves):
    color = 'red' if turn_step < 2 else 'blue'
    for move in moves:
        pygame.draw.circle(screen, color,
                           (move[0] * square_size + square_size // 2, move[1] * square_size + square_size // 2),
                           square_size // 10)


# draw captured pieces on side of screen
def draw_captured():
    # White's captured pieces on the right sidebar
    for i, captured_piece in enumerate(captured_pieces_white):
        index = piece_list.index(captured_piece)
        captured_image = pygame.transform.scale(small_black_images[index], (square_size * 0.4, square_size * 0.4))
        screen.blit(captured_image,
                    (8 * square_size + square_size * 0.1, i * square_size * 0.5))

    # Black's captured pieces
    for i, captured_piece in enumerate(captured_pieces_black):
        index = piece_list.index(captured_piece)
        captured_image = pygame.transform.scale(small_white_images[index], (square_size * 0.4, square_size * 0.4))
        screen.blit(captured_image,
                    (8 * square_size + square_size * 0.6, i * square_size * 0.5))


# draw a flashing square around king if in check
def draw_check():
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)


def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


# main game loop
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                # Calculate the clicked grid coordinates dynamically
                x_coord = event.pos[0] // square_size
                y_coord = event.pos[1] // square_size
                click_coords = (x_coord, y_coord)

                # Ensure clicks are within the 8x8 grid
                if y_coord < 8:
                    if turn_step <= 1:  # White's turn
                        if click_coords in white_locations:
                            selection = white_locations.index(click_coords)
                            if turn_step == 0:
                                turn_step = 1
                        elif click_coords in valid_moves and selection != 100:
                            white_locations[selection] = click_coords
                            if click_coords in black_locations:
                                black_piece = black_locations.index(click_coords)
                                captured_pieces_white.append(black_pieces[black_piece])
                                if black_pieces[black_piece] == 'king':
                                    winner = 'white'
                                black_pieces.pop(black_piece)
                                black_locations.pop(black_piece)
                            black_options = check_options(black_pieces, black_locations, 'black')
                            white_options = check_options(white_pieces, white_locations, 'white')
                            turn_step = 2
                            selection = 100
                            valid_moves = []
                    else:  # Black's turn
                        if click_coords in black_locations:
                            selection = black_locations.index(click_coords)
                            if turn_step == 2:
                                turn_step = 3
                        elif click_coords in valid_moves and selection != 100:
                            black_locations[selection] = click_coords
                            if click_coords in white_locations:
                                white_piece = white_locations.index(click_coords)
                                captured_pieces_black.append(white_pieces[white_piece])
                                if white_pieces[white_piece] == 'king':
                                    winner = 'black'
                                white_pieces.pop(white_piece)
                                white_locations.pop(white_piece)
                            black_options = check_options(black_pieces, black_locations, 'black')
                            white_options = check_options(white_pieces, white_locations, 'white')
                            turn_step = 0
                            selection = 100
                            valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = check_options(black_pieces, black_locations, 'black')
                white_options = check_options(white_pieces, white_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()
