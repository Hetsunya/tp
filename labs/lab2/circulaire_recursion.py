import turtle
import math

def draw_circle_fractal_recursive(x, y, size, depth, count):
    min_size = 1
    m = 6
    n = 3

    if size > min_size and depth > 0:
        s1 = round(size / n)
        s2 = round(size * (n - 1) / n)

        draw_circle_fractal_recursive(x, y, s1, depth - 1, count)
        for i in range(1, m + 1):
            draw_circle_fractal_recursive(x - round(s2 * math.sin(2 * math.pi / m * i)),
                                          y + round(s2 * math.cos(2 * math.pi / m * i)),
                                          s1, depth - 1, count)

        turtle.up()
        turtle.goto(x, y - size)
        turtle.down()
        turtle.circle(size)

def recursive_main():
    turtle.speed(20000000)
    turtle.hideturtle()
    turtle.title("Recursive Circle Fractal")

    x, y, initial_size, initial_depth, circles_count = 0, 0, 200, 5, 6

    draw_circle_fractal_recursive(x, y, initial_size, initial_depth, circles_count)

    turtle.update()
    turtle.mainloop()

if __name__ == "__main__":
    recursive_main()
