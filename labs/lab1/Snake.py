import pygame
import random

pygame.init()

# Определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Установка размеров экрана
dis_width = 1000
dis_height = 500
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка на Python с ИИ')

# Установка параметров змейки
snake_block = 10
snake_speed = 15


# Определение шрифта и размера текста
font_style = pygame.font.SysFont(pygame.font.get_default_font(), 30)


# Отображение счета
def Your_score(score, player):
    value = font_style.render(f"Счет Игрока {player}: {str(score)}", True, white)
    dis.blit(value, [10 if player == 1 else dis_width - 200, 10])


# Отрисовка змейки
def our_snake(snake_block, snake_list, player):
    for x in snake_list:
        pygame.draw.rect(dis, blue if player == 1 else red, [x[0], x[1], snake_block, snake_block])


# ИИ для движения змейки
def move_ai(snake_head, direction):
    x, y = snake_head
    if direction == 'UP':
        return x, y - snake_block
    elif direction == 'DOWN':
        return x, y + snake_block
    elif direction == 'LEFT':
        return x - snake_block, y
    elif direction == 'RIGHT':
        return x + snake_block, y


# Основная функция
def gameLoop():
    # Инициализация игровых переменных
    game_over = False

    # Инициализация координат змеек
    x1_player1 = dis_width / 4
    y1_player1 = dis_height / 2

    x1_player2 = 3 * dis_width / 4
    y1_player2 = dis_height / 2

    # Инициализация изменений координат
    x1_change_player1 = 0
    y1_change_player1 = 0

    x1_change_player2 = 0
    y1_change_player2 = 0

    # Инициализация длины змеек и скорости роста
    snake_List_player1 = []
    Length_of_snake_player1 = 1

    snake_List_player2 = []
    Length_of_snake_player2 = 1

    # Инициализация направления движения для ИИ
    direction_player1 = 'UP'
    direction_player2 = 'UP'

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # ИИ для игрока 1
        head_player1 = snake_List_player1[-1] if snake_List_player1 else [x1_player1, y1_player1]
        if head_player1[0] < dis_width / 2:
            if head_player1[1] >= dis_height - snake_block:
                direction_player1 = 'UP'
            elif head_player1[1] <= 0:
                direction_player1 = 'DOWN'
        else:
            if head_player1[1] >= dis_height - snake_block:
                direction_player1 = 'UP'
            elif head_player1[1] <= 0:
                direction_player1 = 'DOWN'

        x1_change_player1, y1_change_player1 = move_ai(head_player1, direction_player1)

        # ИИ для игрока 2
        head_player2 = snake_List_player2[-1] if snake_List_player2 else [x1_player2, y1_player2]
        if head_player2[0] < dis_width / 2:
            if head_player2[1] >= dis_height - snake_block:
                direction_player2 = 'UP'
            elif head_player2[1] <= 0:
                direction_player2 = 'DOWN'
        else:
            if head_player2[1] >= dis_height - snake_block:
                direction_player2 = 'UP'
            elif head_player2[1] <= 0:
                direction_player2 = 'DOWN'

        x1_change_player2, y1_change_player2 = move_ai(head_player2, direction_player2)

        x1_player1 += x1_change_player1
        y1_player1 += y1_change_player1

        x1_player2 += x1_change_player2
        y1_player2 += y1_change_player2

        dis.fill(black)
        pygame.draw.line(dis, white, (dis_width / 2, 0), (dis_width / 2, dis_height), 2)

        # Отрисовка змеек
        our_snake(snake_block, snake_List_player1, 1)
        our_snake(snake_block, snake_List_player2, 2)

        # Обработка движения змейки игрока 1
        snake_head_player1 = []
        snake_head_player1.append(x1_player1)
        snake_head_player1.append(y1_player1)
        snake_List_player1.append(snake_head_player1)
        if len(snake_List_player1) > Length_of_snake_player1:
            del snake_List_player1[0]

        # Проверка столкновений игрока 1
        for x in snake_List_player1[:-1]:
            if x == snake_head_player1:
                game_over = True

        # Отображение счета для игрока 1
        Your_score(Length_of_snake_player1 - 1, 1)

        # Обработка движения змейки игрока 2
        snake_head_player2 = []
        snake_head_player2.append(x1_player2)
        snake_head_player2.append(y1_player2)
        snake_List_player2.append(snake_head_player2)
        if len(snake_List_player2) > Length_of_snake_player2:
            del snake_List_player2[0]

        # Проверка столкновений игрока 2
        for x in snake_List_player2[:-1]:
            if x == snake_head_player2:
                game_over = True

        # Отображение счета для игрока 2
        Your_score(Length_of_snake_player2 - 1, 2)

        pygame.display.update()

        # Появление новой еды
        if x1_player1 == x1_player2 and y1_player1 == y1_player2:
            foodx = round(random.randrange(int(dis_width / 2), int(dis_width - snake_block), 10))
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        else:
            foodx = round(random.uniform(0, (dis_width / 2 - snake_block) / 10.0) * 10.0)
            foody = round(random.uniform(0, (dis_height - snake_block) / 10.0) * 10.0)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
