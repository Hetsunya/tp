import pygame
import random
import sys

pygame.init()

# Определение констант
WIDTH, HEIGHT = 1200, 600
CELL_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SEA_BLUE = (0, 119, 190)
SHIPS_COLOR = (0, 33, 55)
HIT_COLOR = (128, 0, 128)  # Фиолетовый цвет для отображения попадания
FONT_SIZE = 20


def draw_shot_result(board, row, col, offset=0):
    if board[row][col] == 'X':
        pygame.draw.rect(screen, HIT_COLOR, (col * CELL_SIZE + offset, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    elif board[row][col] == ' ':
        pygame.draw.rect(screen, BLACK, (col * CELL_SIZE + offset, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))




class SeaBattleGame:
    def __init__(self):
        self.player_board = [[' ' for _ in range(10)] for _ in range(10)]
        self.computer_board = [[' ' for _ in range(10)] for _ in range(10)]
        self.player_ships = {'L': 4, 'C': 3, 'D': 2, 'B': 1}
        self.computer_ships = {'L': 4, 'C': 3, 'D': 2, 'B': 1}
        self.computer_hits = set()
        self.computer_first_shot = False

    def place_ships(self, board):
        ship_types = ['L', 'C', 'C', 'D', 'D', 'D', 'B', 'B', 'B', 'B']
        for ship_type in ship_types:
            self.place_ship(board, ship_type, self.player_ships[ship_type])

    def place_ship(self, board, ship_type, size):
        direction = random.choice(['H', 'V'])
        if direction == 'H':
            row = random.randint(0, 9)
            col = random.randint(0, 10 - size)
            while any(board[row][col + i] != ' ' for i in range(-1, size + 1)
                      if 0 <= col + i < 10):
                row = random.randint(0, 9)
                col = random.randint(0, 10 - size)
            for i in range(size):
                board[row][col + i] = ship_type
        else:
            row = random.randint(0, 10 - size)
            col = random.randint(0, 9)
            while any(board[row + i][col] != ' ' for i in range(-1, size + 1)
                      if 0 <= row + i < 10):
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
                self.computer_board[guess_row][guess_col] = 'X'  # Помечаем попадание компьютера
                self.player_board[guess_row][guess_col] = 'H'  # Помечаем попадание игрока

                if ship_type in self.computer_ships:
                    self.computer_ships[ship_type] -= 1
                    self.computer_ships[ship_type] = max(0, self.computer_ships[ship_type])
                    if self.computer_ships[ship_type] == 0:
                        print(f"You sank an enemy {ship_type}!")
            else:
                print("You missed!")
                self.computer_board[guess_row][guess_col] = 'M'  # Помечаем промах компьютера
                self.player_board[guess_row][guess_col] = 'B'  # Помечаем промах игрока
        else:
            print("Invalid move. Click inside the board.")

        draw_shot_result(self.computer_board, guess_row, guess_col)  # в player_turn

    def computer_turn(self):
        if self.computer_hits:
            x, y = self.computer_hits.pop()
        else:
            if not self.computer_first_shot:
                x, y = self.get_optimal_first_shot()
                self.computer_first_shot = True
            else:
                x, y = self.get_optimal_shot()

        if self.player_board[x][y] != ' ':
            ship_type = self.player_board[x][y]
            print(f"Oh no! The computer hit your {ship_type}!")
            if ship_type != 'M' and ship_type != 'H' and ship_type != 'X':
                self.player_board[x][y] = 'H'  # Помечаем попадание игрока
                self.player_ships[ship_type] -= 1
                if self.player_ships[ship_type] == 0:
                    print(f"The computer sank your {ship_type}!")
                    self.computer_hits.clear()
        else:
            print("Phew! The computer missed!")
            self.player_board[x][y] = 'M'  # Помечаем промах игрока

        draw_shot_result(self.player_board, x, y, WIDTH // 2)  # в computer_turn

    def get_optimal_first_shot(self):
        # Просто выстрелы по диагонали
        return random.choice([(i, i) for i in range(10)])

    def get_optimal_shot(self):
        if self.computer_hits:
            x, y = self.computer_hits.pop()
            potential_shots = [
                (x - 1, y), (x + 1, y),
                (x, y - 1), (x, y + 1)
            ]
            potential_shots = [(i, j) for i, j in potential_shots if
                               0 <= i < 10 and 0 <= j < 10 and (i, j) not in self.computer_hits]
            if potential_shots:
                return random.choice(potential_shots)
            else:
                # Если все окружающие клетки были уже проверены, выберем случайную непроверенную клетку
                unchecked_cells = [(i, j) for i in range(10) for j in range(10) if (i, j) not in self.computer_hits]
                return random.choice(unchecked_cells)
        else:
            # Если попаданий нет, выбираем случайную клетку, не бившуюся ранее
            unchecked_cells = [(i, j) for i in range(10) for j in range(10) if (i, j) not in self.computer_hits]
            return random.choice(unchecked_cells)


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
                    pygame.draw.rect(screen, SHIPS_COLOR, (j * CELL_SIZE + offset, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif board[i][j] == 'X':
                draw_shot_result(board, i, j, offset)  # Перенесено сюда




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
                if WIDTH // 2 <= x < WIDTH and 0 <= y < HEIGHT:
                    # Клик на доске противника
                    game.player_turn(x - WIDTH // 2, y)
                    game.computer_turn()  # Автоматический ход компьютера после хода игрока

                    if all(count == 0 for count in game.computer_ships.values()):
                        draw_text("Congratulations! You won!", WIDTH // 4, HEIGHT // 2)
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        pygame.quit()
                        sys.exit()

                    if all(count == 0 for count in game.player_ships.values()):
                        draw_text("Game over! The computer won.", WIDTH // 4, HEIGHT // 2)
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        pygame.quit()
                        sys.exit()

        screen.fill(BLACK)
        draw_board(game.player_board, 0)
        draw_board(game.computer_board, WIDTH // 2, show_ships=False)
        draw_text("Your Board", 20, HEIGHT - 30)
        draw_text("Computer's Board", WIDTH // 2 + 20, HEIGHT - 30)

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()