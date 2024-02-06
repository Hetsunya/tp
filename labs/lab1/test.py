import os
from random import randrange, choice

# Класс, представляющий различные части поля
class FieldPart:
    main = 'map'
    radar = 'radar'
    weight = 'weight'

# Класс для цветов текста в консоли
class Color:
    yellow2 = '\033[1;35m'
    reset = '\033[0m'
    blue = '\033[0;34m'
    yellow = '\033[1;93m'
    red = '\033[1;93m'
    miss = '\033[0;37m'

# Функция окрашивает текст в заданный цвет
def set_color(text, color):
    return color + text + Color.reset

# Класс, представляющий клетку поля
class Cell:
    empty_cell = set_color(' ', Color.yellow2)
    ship_cell = set_color('■', Color.blue)
    destroyed_ship = set_color('X', Color.yellow)
    damaged_ship = set_color('□', Color.red)
    miss_cell = set_color('•', Color.miss)

# Класс поля, состоящего из трех частей: карты, радара и весов
class Field:
    def __init__(self, size):
        self.size = size
        self.map = [[Cell.empty_cell for _ in range(size)] for _ in range(size)]
        self.radar = [[Cell.empty_cell for _ in range(size)] for _ in range(size)]
        self.weight = [[1 for _ in range(size)] for _ in range(size)]

    # Отрисовка поля в консоли
    def draw_field(self, element):
        # ... (опущено для краткости)

# Класс игры
class Game:
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
    ships_rules = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    field_size = len(letters)

    def __init__(self):
        self.players = []
        self.current_player = None
        self.next_player = None
        self.status = 'prepare'

    # Функция проверки статуса игры
    def status_check(self):
        # ... (опущено для краткости)

    # Добавление игрока в игру
    def add_player(self, player):
        player.field = Field(Game.field_size)
        player.enemy_ships = list(Game.ships_rules)
        player.field.recalculate_weight_map(player.enemy_ships)
        self.players.append(player)

    # Настройка расстановки кораблей
    def ships_setup(self, player):
        # ... (опущено для краткости)

# Класс игрока
class Player:
    def __init__(self, name, is_ai, skill, auto_ship):
        self.name = name
        self.is_ai = is_ai
        self.auto_ship_setup = auto_ship
        self.skill = skill
        self.message = []
        self.ships = []
        self.enemy_ships = []
        self.field = None

    # Получение ввода от игрока
    def get_input(self, input_type):
        # ... (опущено для краткости)

    # Совершение выстрела
    def make_shot(self, target_player):
        # ... (опущено для краткости)

    # Принятие выстрела от противника
    def receive_shot(self, shot):
        # ... (опущено для краткости)

# Класс корабля
class Ship:
    def __init__(self, size, x, y, rotation):
        # ... (опущено для краткости)

# Главная часть программы
if __name__ == '__main__':
    players = [
        Player(name='Username', is_ai=False, auto_ship=True, skill=1),
        Player(name='AI', is_ai=True, auto_ship=True, skill=1)
    ]

    game = Game()

    while True:
        game.status_check()

        if game.status == 'prepare':
            game.add_player(players.pop(0))

        if game.status == 'in game':
            Game.clear_screen()
            game.current_player.message.append("Ждём приказа: ")
            game.draw()
            game.current_player.message.clear()
            shot_result = game.current_player.make_shot(game.next_player)

            if shot_result == 'miss':
                game.next_player.message.append('На этот раз {}, промахнулся! '.format(game.current_player.name))
                game.next_player.message.append('Ваш ход {}!'.format(game.next_player.name))
                game.switch_players()
                continue
            elif shot_result == 'retry':
                game.current_player.message.append('Попробуйте еще раз!')
                continue
            elif shot_result == 'get':
                game.current_player.message.append('Отличный выстрел, продолжайте!')
                game.next_player.message.append('Наш корабль попал под обстрел!')
                continue
            elif shot_result == 'kill':
                game.current_player.message.append('Корабль противника уничтожен!')
                game.next_player.message.append('Плохие новости, наш корабль был уничтожен :(')
                continue

        if game.status == 'game over':
            Game.clear_screen()
            game.next_player.field.draw_field(FieldPart.main)
            game.current_player.field.draw_field(FieldPart.main)
            print('Это был последний корабль {}'.format(game.next_player.name))
            print('{} выиграл матч! Поздравления!'.format(game.current_player.name))
            break

    print('Спасибо за игру!')
    input('')
