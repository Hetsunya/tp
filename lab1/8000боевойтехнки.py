import pygame
import random
import sys

pygame.init()

# Определение констант
WIDTH, HEIGHT = 900, 600
CELL_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SEA_BLUE = (0, 119, 190)
SHIP_COLORS = [(255, 175, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255)]
HIT_COLOR = (255, 0, 0)
FONT_SIZE = 20


class SeaBattleGame:
    def __init__(self):
        self.player_board = [[' ' for _ in range(10)] for _ in range(10)]
        self.computer_board = [[' ' for _ in range(10)] for _ in range(10)]
        self.player_ships = {'L': 1, 'C': 2, 'D': 3, 'B': 4}
        self.computer_ships = {'L': 1, 'C': 2, 'D': 3, 'B': 4}

    def place_ships(self, board):
        for ship_type, size in self.player_ships.items():
            self.place_ship(board, ship_type, size)

    def place_ship(self, board, ship_type, size):
        for i in range(1, 2):
            direction = random.choice(['H', 'V'])
            if direction == 'H':
                row = random.randint(0, 9)
                col = random.randint(0, 10 - size)
                while any(board[row][col + i] == 'X' for i in range(size)):
                    row = random.randint(0, 9)
                    col = random.randint(0, 10 - size)
                for i in range(size):
                    board[row][col + i] = ship_type
            else:
                row = random.randint(0, 10 - size)
                col = random.randint(0, 9)
                while any(board[row + i][col] == 'X' for i in range(size)):
                    row = random.randint(0, 10 - size)
                    col = random.randint(0, 9)
                for i in range(size):
                    board[row + i][col] = ship_type

    def player_turn(self, x, y):
        guess_row = y // CELL_SIZE
        guess_col = x // CELL_SIZE

        if 0 <= guess_row < 10 and 0 <= guess_col < 10:
            if self.computer_board[guess_row][guess_col] != ' ':
                ship_type = self.computer_board[guess_row][guess_col]
                print(f"Congratulations! You hit an enemy {ship_type}!")
                self.computer_ships[ship_type] -= 1
                self.computer_ships[ship_type] = max(0, self.computer_ships[ship_type])
                self.computer_board[guess_row][guess_col] = 'H'
                if self.computer_ships[ship_type] == 0:
                    print(f"You sank an enemy {ship_type}!")
            else:
                print("You missed!")
        else:
            print("Invalid move. Click inside the board.")

    def computer_turn(self):
        guess_row = random.randint(0, 9)
        guess_col = random.randint(0, 9)

        if self.player_board[guess_row][guess_col] != ' ':
            ship_type = self.player_board[guess_row][guess_col]
            print(f"Oh no! The computer hit your {ship_type}!")
            self.player_ships[ship_type] -= 1
            self.player_ships[ship_type] = max(0, self.player_ships[ship_type])
            self.player_board[guess_row][guess_col] = 'H'
            if self.player_ships[ship_type] == 0:
                print(f"The computer sank your {ship_type}!")
        else:
            print("Phew! The computer missed!")


# Инициализация игрового окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sea Battle Game")

font = pygame.font.SysFont(None, FONT_SIZE)


def draw_board(board, offset, show_ships=True):
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen, SEA_BLUE, (j * CELL_SIZE + offset, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, WHITE, (j * CELL_SIZE + offset, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

            if show_ships:
                ship_type = board[i][j]
                if ship_type != ' ':
                    color_index = ord(ship_type) - ord('A')
                    color = SHIP_COLORS[color_index] if 0 <= color_index < len(SHIP_COLORS) else WHITE
                    pygame.draw.rect(screen, color, (j * CELL_SIZE + offset, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))


def main():
    game = SeaBattleGame()
    game.place_ships(game.player_board)
    game.place_ships(game.computer_board)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                game.player_turn(x, y)

                if all(count == 0 for count in game.computer_ships.values()):
                    draw_text("Congratulations! You won!", WIDTH // 4, HEIGHT // 2)
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    pygame.quit()
                    sys.exit()

                game.computer_turn()

                if all(count == 0 for count in game.player_ships.values()):
                    draw_text("Game over! The computer won.", WIDTH // 4, HEIGHT // 2)
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    pygame.quit()
                    sys.exit()

        screen.fill(BLACK)
        draw_board(game.player_board, 0)
        # draw_board(game.computer_board, WIDTH // 2, show_ships=False)
        draw_text("Your Board", 20, HEIGHT - 30)
        # draw_text("Computer's Board", WIDTH // 2 + 20, HEIGHT - 30)

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
