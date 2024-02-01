import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размер окна
width, height = 800, 600

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Треугольник Серпинского")

def draw_sierpinski_triangle(vertices, order):
    if order == 0:
        pygame.draw.polygon(screen, red, vertices)
    else:
        mid1 = ((vertices[0][0] + vertices[1][0]) / 2, (vertices[0][1] + vertices[1][1]) / 2)
        mid2 = ((vertices[1][0] + vertices[2][0]) / 2, (vertices[1][1] + vertices[2][1]) / 2)
        mid3 = ((vertices[2][0] + vertices[0][0]) / 2, (vertices[2][1] + vertices[0][1]) / 2)

        draw_sierpinski_triangle([vertices[0], mid1, mid3], order - 1)
        draw_sierpinski_triangle([mid1, vertices[1], mid2], order - 1)
        draw_sierpinski_triangle([mid3, mid2, vertices[2]], order - 1)

# Вершины начального треугольника
initial_vertices = [(400, 100), (200, 500), (600, 500)]

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(white)

    # Отрисовка треугольника Серпинского
    draw_sierpinski_triangle(initial_vertices, order=4)

    # Обновление экрана
    pygame.display.flip()
