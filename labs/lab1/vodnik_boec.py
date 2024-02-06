import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Создание игрового поля
player_grid = [[' '] * GRID_SIZE for _ in range(GRID_SIZE)]
ai_grid = [[' '] * GRID_SIZE for _ in range(GRID_SIZE)]

# Функция отрисовки сетки
def draw_grid(surface, grid, offset):
    for i in range(GRID_SIZE + 1):
        pygame.draw.line(surface, WHITE, (offset, i * CELL_SIZE + offset),
                         (GRID_SIZE * CELL_SIZE + offset, i * CELL_SIZE + offset))
        pygame.draw.line(surface, WHITE, (i * CELL_SIZE + offset, offset),
                         (i * CELL_SIZE + offset, GRID_SIZE * CELL_SIZE + offset))

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 'X':
                pygame.draw.rect(surface, BLUE, (col * CELL_SIZE + offset, row * CELL_SIZE + offset,
                                                CELL_SIZE, CELL_SIZE))
            elif grid[row][col] == 'O':
                pygame.draw.rect(surface, RED, (col * CELL_SIZE + offset, row * CELL_SIZE + offset,
                                               CELL_SIZE, CELL_SIZE))

# Функция размещения кораблей на поле
def place_ships(grid):
    for _ in range(5):  # 5 кораблей
        while True:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if grid[row][col] == ' ':
                grid[row][col] = 'X'
                break

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Морской бой')

# Размещение кораблей на полях игроков
place_ships(player_grid)
place_ships(ai_grid)

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Отрисовка игровых полей
    draw_grid(screen, player_grid, 0)
    draw_grid(screen, ai_grid, WIDTH // 2)

    pygame.display.flip()
