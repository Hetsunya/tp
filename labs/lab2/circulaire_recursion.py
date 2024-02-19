import turtle
import math

def draw_circle_fractal(x, y, size, depth):
    min_size = 5
    m = 6
    n = 3

    for _ in range(depth):
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

            draw_circle_fractal(new_x, new_y, s1, depth - 1)
        draw_circle_fractal(x, y, s1, depth - 1)


def main():
    turtle.speed(200)
    turtle.hideturtle()
    turtle.title("Circle Fractal")

    x, y, initial_size, initial_depth = 0, 0, 400, 3

    draw_circle_fractal(x, y, initial_size, initial_depth)

    turtle.done()

if __name__ == "__main__":
    main()
