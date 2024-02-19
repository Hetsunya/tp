import turtle
import math

def draw_circle_fractal(x, y, size, depth, count):
    min_size = 5
    m = 6
    n = 3

    if size > min_size:
        s1 = round(size / n)
        s2 = round(size * (n - 1) / n)

        # Рисуем центральную окружность перед циклом
        turtle.up()
        turtle.goto(x, y - size)
        turtle.down()
        turtle.circle(size)

        for i in range(1, m + 1):
            new_x = x - round(s2 * math.sin(2 * math.pi / m * i))
            new_y = y + round(s2 * math.cos(2 * math.pi / m * i))

            draw_circle_fractal(new_x, new_y, s1, depth - 1, count)

def recursive_main():
    turtle.speed(200)
    turtle.hideturtle()
    turtle.title("Recursive Circle Fractal")

    x, y, initial_size, initial_depth, circles_count = 0, 0, 200, 3, 3

    for _ in range(circles_count):
        draw_circle_fractal(x, y, initial_size, initial_depth, circles_count)
        x += 300  # Перемещаемся на следующую позицию

    turtle.done()

if __name__ == "__main__":
    recursive_main()
