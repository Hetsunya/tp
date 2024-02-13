import turtle
import math

# turtle.tracer(0)   # ДЛЯ СКИПА

def draw_circle_fractal(x, y, size, depth, count):
    min_size = 1
    m = 6
    n = 3

    if size > min_size:
        s1 = round(size / n)
        s2 = round(size * (n - 1) / n)

        draw_circle_fractal(x,
                            y,
                            s1, depth - 1, count)
        for i in range(1, m + 1):
            draw_circle_fractal(x - round(s2 * math.sin(2 * math.pi / m * i)),
                                y + round(s2 * math.cos(2 * math.pi / m * i)),
                                s1, depth - 1, count)



        turtle.up()
        turtle.goto(x, y - size)
        turtle.down()
        turtle.circle(size)

def main():
    turtle.speed(20000000)
    turtle.hideturtle()
    turtle.title("Circle Fractal")

    x, y, initial_size, initial_depth, circles_count = 0, 0, 200, 3, 6

    draw_circle_fractal(x, y, initial_size, initial_depth, circles_count)

    turtle.done()

    # turtle.update()# ДЛЯ СКИПА

    # turtle.mainloop()  #ДЛЯ СКИПА

if __name__ == "__main__":
    main()